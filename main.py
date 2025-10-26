def get_book_text(path):

    with open(path) as f:
        book_text = f.read()
    return book_text 

from stats import get_num_words

def main():

    text=get_book_text("./books/frankenstein.txt")
    length=get_num_words(text)
    print(f"Found", length, "total words")

main()
