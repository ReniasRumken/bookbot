from stats import get_book_text, count_characters, sorted_list
import sys
    
def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        sys.exit(1)
        
    file_contents, num_words = get_book_text(sys.argv[1])
    #print(f"{num_words} words found in the document")
    char_dict = count_characters(file_contents)
    list = sorted_list(char_dict)
    #print(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in list:
        if char_dict["char"].isalpha():
            print(f'{char_dict["char"]}: {char_dict["count"]}')

    print("============= END ===============")


main()
