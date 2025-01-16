#grep

import sys

def search_pattern(pattern, filename):
    try:
        with open(filename, 'r') as file:
            # Search each line for the pattern
            for line_num, line in enumerate(file, 1):
                if pattern in line:
                    # Remove trailing newline and print matching line
                    print(f"{line_num}: {line.rstrip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep.py pattern filename")
        sys.exit(1)
    
    pattern = sys.argv[1]
    filename = sys.argv[2]
    search_pattern(pattern, filename)