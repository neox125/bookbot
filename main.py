import sys
from stats import text_from_book, get_chars_dict,sorted_chars_dict,get_book_text,report_format

def main():
    filepath = sys.argv[1]   # Replace with the actual path to the book file
    book_text = get_book_text(filepath)
    num_words = text_from_book(book_text)
    chars_dict= get_chars_dict(book_text)
    sorted_list = sorted_chars_dict(chars_dict)
    report_format(filepath,num_words,sorted_list) 
    
if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()


  
    