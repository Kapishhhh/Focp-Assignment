# wc
import sys

def count_file_stats(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            lines = contents.splitlines()
            words = contents.split()
            
            # Count statistics
            num_lines = len(lines)
            num_words = len(words)
            num_chars = len(contents)
            
            # Print results in format similar to Unix wc
            print(f"{num_lines:8d} {num_words:8d} {num_chars:8d} {filename}")
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wc.py filename")
        sys.exit(1)
    
    count_file_stats(sys.argv[1])