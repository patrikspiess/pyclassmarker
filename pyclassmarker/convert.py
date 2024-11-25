"""
The ClassMarker convert module
"""

import csv
import json
import sys
from pathlib import Path

from rich import print as rich_print
from rich.console import Group
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text


def list_split(full_list, chunk_size):
    """
    Splits a list into chunks

    Args:
        full_list:  The list to split
        chunk_size: The size of each chunk (last one may be shorter)

    Returns:
        The chunks
    """
    for i in range(0, len(full_list), chunk_size):
        yield full_list[i : i + chunk_size]


TO_TRANSLATE = {
    "freetext": [
        "Question",
        "Answer A",
        "Answer B",
        "Answer C",
        "Answer D",
        "Answer E",
        "Answer F",
        "Answer G",
        "Answer H",
        "Answer I",
        "Answer J",
        "Answer K",
        "Answer L",
        "Answer M",
        "Answer N",
        "Answer O",
        "Answer P",
        "Answer Q",
        "Answer R",
        "Answer S",
        "Answer T",
    ],
    "matching": [
        "Question",
        "A Clue",
        "A Match",
        "B Clue",
        "B Match",
        "C Clue",
        "C Match",
        "D Clue",
        "D Match",
        "E Clue",
        "E Match",
        "F Clue",
        "F Match",
        "G Clue",
        "G Match",
        "H Clue",
        "H Match",
        "I Clue",
        "I Match",
        "J Clue",
        "J Match",
        "K Clue",
        "K Match",
        "L Clue",
        "L Match",
        "M Clue",
        "M Match",
        "N Clue",
        "N Match",
        "O Clue",
        "O Match",
        "P Clue",
        "P Match",
        "Q Clue",
        "Q Match",
        "R Clue",
        "R Match",
        "S Clue",
        "S Match",
        "T Clue",
        "T Match",
        # "A Incorrect",    # ???
        # "B Incorrect",    # ???
        # "C Incorrect",    # ???
        # "D Incorrect",    # ???
        # "E Incorrect",    # ???
    ],
    "multiplechoice": [
        "Question",
        "Answer A",
        "Answer B",
        "Answer C",
        "Answer D",
        "Answer E",
        "Answer F",
        "Answer G",
        "Answer H",
        "Answer I",
        "Answer J",
    ],
    "multipleresponse": [
        "Question",
        "Answer A",
        "Answer B",
        "Answer C",
        "Answer D",
        "Answer E",
        "Answer F",
        "Answer G",
        "Answer H",
        "Answer I",
        "Answer J",
    ],
    "truefalse": [
        "Question",
        "Answer A",
        "Answer B",
    ],
}


def print_multiplechoice(line: str) -> None:
    """Print a multiple choice question"""
    answers = "\n".join([f"- {t}" for t in line[9::]])
    panel_group = Group(
        Panel(line[7], style="white", title=Text("Question", style="white"), title_align="left"),
        Panel(
            Markdown(
                answers,
            ),
            style="green",
            title=Text("Answers", style="green"),
            title_align="left",
        ),
        Panel(
            line[4],
            style="green",
            title=Text("Correct Feedback", style="green"),
            title_align="left",
        ),
        Panel(
            line[5],
            style="green",
            title=Text("Incorrect Feedback", style="green"),
            title_align="left",
        ),
    )
    rich_print(Panel(panel_group, title_align="left", style="blue"))


def main():  # pylint: disable=too-many-locals
    """
    The main function in spaghetti style
    """

    if len(sys.argv) < 2:
        raise SystemExit("Give a ClassMarker CSV file to read")

    import_file_path = Path(sys.argv[1])

    export_path = Path(import_file_path).resolve().parent
    export_file_name = Path(import_file_path).stem
    json_file_name = export_path / (export_file_name + ".json")
    text_file_name = export_path / (export_file_name + ".txt")

    print(f"File to read is {import_file_path}")
    print(f"Path to save export file to is {export_path}")
    print(f"Filename for export is {export_file_name}_#")
    print(f"Filename for JSON is {json_file_name}")
    print(f"Filename for TEXT is {text_file_name}")

    headers = {}  # A dictionary containing the different headers as a list
    lines = []  # A list of lines from the CSV. A line is another list (one element per column)
    questions_as_dict = []  # A list of dictionaries of questions
    questions_categorized = {}
    text: str = ""

    with open(import_file_path, newline="", encoding="UTF-8") as f:
        reader = csv.reader(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            lines.append(row)

    # Rich print
    for line in lines:
        # print(line)
        if not line:  # ignore empty lines
            continue

        if line[0].startswith("Question Type:"):  # it's a header line
            start = 15
            headers[line[0][start:]] = line
            continue

        # print_multiplechoice(line)
        question = {}
        for i, col in enumerate(headers[line[0]]):
            if i == 0:
                col = col[:13]

            try:
                value = " ".join(line[i].split())  # Remove non-braking spaces (\u00a0)

            except IndexError:
                # value = ""
                continue

            question[col] = value

            if col in TO_TRANSLATE[line[0]] and value:
                text += value
                text += "\n" + 100 * "-" + "\n"

        text += 100 * "=" + "\n"

        questions_as_dict.append(question)
        if line[0] not in questions_categorized:
            questions_categorized[line[0]] = []

        questions_categorized[line[0]].append(line)

    print(f"Lines in file: {len(lines)}")
    print("Headers: " + ", ".join(headers.keys()))
    for cat, questions in questions_categorized.items():
        print(f"{cat}: {len(questions)}")

    # Write questions to JSON
    with json_file_name.open("w", encoding="UTF-8") as out_file:
        json.dump(questions_as_dict, out_file, indent=4, ensure_ascii=False)

    # Write text to file
    with text_file_name.open("w", encoding="UTF-8") as out_file:
        out_file.write(text)

    # # Generate chunks from the whole list
    # chunk_size = 50
    # chunks = list(list_split(lines, chunk_size))
    # print(f"Count of files (chunks) to write is {len(chunks)}")

    # # write to csv
    # for i, chunk in enumerate(chunks, start=1):
    #     file_name = export_path / Path(f"{export_file_name}_{i}.csv")
    #     print(f"Writing to file {file_name}")
    #     with open(file_name, "w", newline="", encoding="UTF-8") as f:
    #         writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    #         writer.writerow(header)
    #         for line in chunk:
    #             writer.writerow(line)


if __name__ == "__main__":
    main()
