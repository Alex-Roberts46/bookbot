def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

def main():
    book = "./books/frankenstein.txt"
    from stats import get_num_words
    from stats import counting_characters
    from stats import character_sort
    book_text = get_book_text(book)
    num_words = get_num_words(book_text)
    characters = counting_characters(book_text)
    sorted = character_sort(characters)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for char_dict in sorted:
        print (f"{char_dict["letter"]}: {char_dict["count"]}")
    print(f"============= END ===============")

main()