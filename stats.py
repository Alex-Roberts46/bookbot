def get_num_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def counting_characters(book_text):
    characters = {}
    lowercase = book_text.lower()
    for letter in lowercase:
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters
    