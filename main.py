def get_book_count(book_text):
    #"""Counts the total number of words in a text file."""
    num_words = 0
    for line in book_text.splitlines():
        num_words += len(line.split())
    return num_words    
def get_book_text(file_path):
    #"""Reads the content of a book file and returns it as a string."""
    with open(file_path) as f:
        book_text = f.read()
    return (book_text)
def main():
    try:
        book_text = get_book_text("books/frankenstein.txt")
        book_count = get_book_count(book_text)
        print(f"{book_count} words found in the document")
    except FileNotFoundError:
        print("Error: File not found. Please check the path and try again.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
if __name__ == "__main__":
    main()