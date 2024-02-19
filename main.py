def main():
    book = book_path("books/frankenstein.txt")
    print(book)




def book_path(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents




main()