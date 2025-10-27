def get_book_text(path):

    with open(path) as f:
        book_text = f.read()
    return book_text 

from stats import get_num_words, count_characters, dictionary_to_list, sort_on
import sys

def main():

    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    else:
        
        path_to_book = sys.argv[1]
        text = get_book_text(path_to_book)
        length = get_num_words(text)
        dict_characters = count_characters(text)
        sorted_list = dictionary_to_list(dict_characters)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_book}...")
        print("----------- Word Count ----------")
        print(f"Found", length, "total words")
        print("----------- Character Count ----------")
        for item in sorted_list:
            if item["char"].isalpha() == True:
                print(f"{item["char"]}: {item["num"]}")
            else:
                continue
        print("============= END ===============")
main()
