book = "./books/frankenstein.txt"

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents
    
def get_num_words(book_text):
    book_text = get_book_text(book)
    words = book_text.split()
    num_words = len(words)
    return num_words

def main():
    book_text = get_book_text(book)
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")


main()