def get_book_text(file_path):
    #"""Reads the content of a book file and returns it as a string."""
    with open(file_path) as f:
        book_text = f.read()
    print (book_text)
def main():
    try:
        book_text = get_book_text("books/frankenstein.txt")
    except FileNotFoundError:
        print("Error: File not found. Please check the path and try again.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
if __name__ == "__main__":
    main()