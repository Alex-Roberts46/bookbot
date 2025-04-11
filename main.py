def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

def main():
    book = "./books/frankenstein.txt"
    book_text = get_book_text(book)
    print(book_text)

main()