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

#def sort_on(dict):
    #return dict["num"]
#char_count = get_char_count(book_text)
#sorted_chars = []
#for key, value in char_count.items():
    #sorted = {"char": key, "num": value}
    #sorted_chars.append(sorted)
def sort_on(dict):
    return dict["num"]
def processed_chars(char_count):
    processed_list = []
    for key, value in char_count.items():
        sorted = {"char": key, "num": value}
        processed_list.append(sorted)
    processed_list.sort(key=sort_on, reverse=True)
    return processed_list


