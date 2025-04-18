def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

def main():
    book = "./books/frankenstein.txt"
    from stats import get_num_words
    from stats import counting_characters
    book_text = get_book_text(book)
    num_words = get_num_words(book_text)
    characters = counting_characters(book_text)
    print(f"{num_words} words found in the document")
    print (f"{characters}")

main()