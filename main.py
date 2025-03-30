import sys
from stats import get_book_text, num_words, count_characters, chars_dict_to_sorted_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    words_list = num_words(text)
    num_of_words = len(words_list)
    char_counts = count_characters(text)
    
    # Get the sorted list of character dictionaries
    sorted_chars = chars_dict_to_sorted_list(char_counts)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    
    # Print each alphabetic character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()

