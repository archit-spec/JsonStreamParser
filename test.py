from parser import Parser

def test_updated_parser():
    stream = ['{ "a" : null}']

    parser = Parser()
    
    for i, chunk in enumerate(stream, 1):
        result = next(parser.parse([chunk]))
        print(f"Chunk {i}: '{chunk}'")
        print(f"Output: {result}")
        print()

if __name__ == "__main__":
    test_updated_parser()