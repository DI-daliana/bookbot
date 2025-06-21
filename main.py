import sys

if len(sys.argv)!=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    contents = " "
    with open(filepath) as f:
        contents = f.read()
    return contents

from stats import get_string
from stats import count_characters 
from stats import sorted_dic

def main():
    filepath = sys.argv[1]
    contents = get_book_text(filepath)
    char_count = count_characters(contents)
    report = sorted_dic(char_count)

    print("================BOOKBOT===============")
    print(f"Analyzing book found at {filepath}...")
    print("-------------Word Count------------")
    print(f"Found {get_string(contents)} total words")
    print("-------Character  Count------")
    for pair in report:
        print(f"{pair["char"]}: {pair["num"]}")

main()

