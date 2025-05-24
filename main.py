def get_book_text(file_path):
    """Reads the content of a book file and returns it as a string."""
    with open(file_path) as f:
        book_text = f.read()
    return (book_text)
from stats import get_char_count
from stats import get_book_count
from stats import processed_chars
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    try:
        book_text = get_book_text(book)
        book_count = get_book_count(book_text)
        char_count = get_char_count(book_text)
        sorted_chars = processed_chars(char_count)
        print("============ BOOKBOT ============")
        print("Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        print(f"Found {book_count} total words")
        print("--------- Character Count -------")
        for char in sorted_chars:
            if char["char"].isalpha():
                print(f"{char['char']}: {char['num']}")
        print("============= END ===============")
        #print(f"{book_count} words found in the document")
        #for char, count in char_count.items():
            #print(f"'{char}': {count}")
    except FileNotFoundError:
        print("Error: File not found. Please check the path and try again.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
if __name__ == "__main__":
    main()