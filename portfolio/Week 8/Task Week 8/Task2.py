# diff

import sys

def compare_files(file1_name, file2_name):
    try:
        with open(file1_name, 'r') as file1, open(file2_name, 'r') as file2:
            file1_contents = file1.read()
            file2_contents = file2.read()
            
            if file1_contents == file2_contents:
                print("Files are identical")
            else:
                print("Files differ")
                
                # Compare line by line to show differences
                file1_lines = file1_contents.splitlines()
                file2_lines = file2_contents.splitlines()
                
                for i, (line1, line2) in enumerate(zip(file1_lines, file2_lines), 1):
                    if line1 != line2:
                        print(f"\nDifference at line {i}:")
                        print(f"< {line1}")
                        print(f"> {line2}")
                
                # Handle files of different lengths
                if len(file1_lines) != len(file2_lines):
                    print("\nFiles have different number of lines:")
                    print(f"{file1_name}: {len(file1_lines)} lines")
                    print(f"{file2_name}: {len(file2_lines)} lines")
                    
    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff.py file1 file2")
        sys.exit(1)
    
    compare_files(sys.argv[1], sys.argv[2])