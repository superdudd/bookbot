def get_book_count(book_text):
    #"""Counts the total number of words in a text file."""
    return len(book_text.split()) 
def get_char_count(book_text):
    #"""Counts the number of times a character appears in a text file."""
    # Example: Count the number of times 'a' appears
    char_count = {}
    for char in book_text:
        char_lower =str.lower(char)
        if char_lower in char_count:
            char_count[char_lower] += 1
        else:
            char_count[char_lower] = 1
    return char_count
