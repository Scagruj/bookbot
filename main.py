def main():
    book = book_path("books/frankenstein.txt")
    words_count = count_words(book)
    letters_count = count_letters(book)
    new_list = [{'letter': key, 'num': value}for key, value in letters_count.items()]
    new_list.sort(reverse=True, key=sort_on)
    print("-- Begin report of books/frankenstein.txt --")
    print(f"{words_count} words found in the document")
    
    for dict in new_list:
        if dict['letter'].isalpha():
            print(f"The '{dict['letter']}' character was found {dict['num']} times")
    print("--- End report ---")
    



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
    return dict["num"]

main()