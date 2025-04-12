def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

def main():
    book = "./books/frankenstein.txt"
    book_text = get_book_text(book)
    words = book_text.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")


main()