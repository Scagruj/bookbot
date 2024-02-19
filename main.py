def main():
    book = book_path("books/frankenstein.txt")
    words_count = count_words(book)
    letters_count = count_letters(book)
    print("-- Begin report of books/frankenstein.txt --")
    print(f"{words_count} words found in the document")
    print(f"The {letters_count} character was found {words_count} times")


def book_path(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(book):
    words = book.split()
    counted = len(words)
    return counted

def count_letters(book):
    new_dict = {}
    book = book.lower()
    for letter in book:
        if letter in new_dict: 
            new_dict[letter] += 1
        else:
            new_dict[letter] = 1
            
    return new_dict

def sort_on(dict):
    return dict[""]

main()