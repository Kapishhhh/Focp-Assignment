# spell
import sys
import string
import re

def load_dictionary(dict_path='words.txt'):
    """Load dictionary words from file"""
    try:
        with open(dict_path, 'r') as file:
            return {word.lower().strip() for word in file}
    except FileNotFoundError:
        print(f"Error: Dictionary file '{dict_path}' not found")
        sys.exit(1)

def check_spelling(filename, dictionary):
    try:
        with open(filename, 'r') as file:
            content = file.read().lower()
            
            # Remove punctuation and split into words
            # Using regex to handle contractions and hyphenated words
            words = re.findall(r"[a-z]+(?:'[a-z]+)?(?:-[a-z]+)?", content.lower())
            
            # Find words not in dictionary
            misspelled = sorted(set(word for word in words if word not in dictionary))
            
            # Print results
            if misspelled:
                print("Possible misspelled words:")
                for word in misspelled:
                    print(word)
            else:
                print("No spelling errors found")
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python spell.py filename")
        sys.exit(1)
    
    # Load dictionary and check spelling
    dictionary = load_dictionary()
    check_spelling(sys.argv[1], dictionary)