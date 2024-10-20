import argparse
import random
import json
from parser import Parser 

def chunk_string(s, min_size=1, max_size=3):
    """Split a string into chunks of random size between min_size and max_size."""
    chunks = []
    while s:
        size = random.randint(min_size, min(max_size, len(s)))
        chunks.append(s[:size])
        s = s[size:]
    return chunks

def main():
    parser = argparse.ArgumentParser(description="Parse a JSON string or file using a streaming parser.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-s', '--string', type=str, help="The JSON string to parse")
    group.add_argument('-f', '--file', type=str, help="Path to the JSON file to parse")
    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as f:
            json_input = f.read()
    else:
        json_input = args.string

    chunks = chunk_string(json_input)
    json_parser = Parser()

    print("Input chunks:")
    for i, chunk in enumerate(chunks, 1):
        print(f"Chunk {i}: '{chunk}'")

    print("\nParsing results:")
    for i, result in enumerate(json_parser.parse(chunks), 1):
        print(f"After chunk {i}: {result}")

if __name__ == "__main__":
    main()
