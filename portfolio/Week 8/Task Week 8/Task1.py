# nl

import sys

def number_lines(filename):
    try:
        with open(filename, 'r') as file:
            # Enumerate starting from 1, print line numbers
            for line_num, line in enumerate(file, 1):
                print(f"{line_num:6d}\t{line}", end='')
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nl.py filename")
        sys.exit(1)
    
    number_lines(sys.argv[1])