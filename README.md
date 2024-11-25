# pyClassMarker

pyClassMarker is a Python library for dealing with [ClassMarker](https://www.classmarker.com/)
files.

## Installation

Clone the repository from GitHub and install it with Poetry to create its virtual environment.

```bash
git clone git@github.com:patrikspiess/pyclassmarker.git
cd pyclassmarker
poetry install
```

## Usage

Either run the convert command (suggested):

```bash
poetry run convert <ClassMarker CSV file>
```

Or run the convert script:

```bash
poetry run python pyclassmarker\convert.py <ClassMarker CSV file>
```

## Data handling

### Input files

You may use the *data* directory to put your ClassMarker files into. This directory will not get
published to the GitHub repository.

### Output files

Output files wil be placed in the directory where the input file was specified.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

If anyone is willing to write some tests please use pytest and pytest-cov and feel free.

## License

[MIT License](https://choosealicense.com/licenses/mit/)

>Copyright (c) [2024] [Patrik Spiess]
>
>Permission is hereby granted, free of charge, to any person obtaining a copy
>of this software and associated documentation files (the "Software"), to deal
>in the Software without restriction, including without limitation the rights
>to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
>copies of the Software, and to permit persons to whom the Software is
>furnished to do so, subject to the following conditions:
>
>The above copyright notice and this permission notice shall be included in all
>copies or substantial portions of the Software.
>
>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
>IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
>FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
>AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
>LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
>OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
>SOFTWARE.