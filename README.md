# Streaming JSON Parser

implements a streaming JSON parser in Python. It can parse JSON data chunk by chunk for parsing json streams

## Features

- Stream parsing of JSON data
- Supports objects, strings, and numbers
- Can parse from file or string as argument

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/archit-spec/jsonstreamParser
   cd streaming-json-parser
   ```

2. No additional dependencies are required as this parser uses only Python standard libraries.

## Usage

### As a Python module

```python
from parser import Parser

# Example with a file
with open('data.json', 'r') as file:
    parser = Parser()
    for parsed_data in parser.parse(file):
        print(parsed_data)

# Example with a list of chunks
chunks = ['{', '"key"', ': "value"', '}']
parser = Parser()
for parsed_data in parser.parse(chunks):
    print(parsed_data)
```

### Command Line Interface

The `cli.py` script provides a command-line interface to the parser.

```
python cli.py [-f FILE -s STRING]
# example :
python3 cli.py -s '{"x a": 333.354, "himm": "noo'
```








