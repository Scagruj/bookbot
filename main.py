def main():
    book = book_path("books/frankenstein.txt")
    words_count = count_words(book)
    print(f"{words_count} words in the Frankenstein book")




def book_path(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(book):
    words = book.split()
    counted = len(words)
    return counted


main()