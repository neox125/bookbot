def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def text_from_book(book_text):
    num_words = len(book_text.split())
    return(num_words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

#def sorted_chars_dict(chars_dict):
 #   sorted_chars = sorted(chars_dict.items(), key=lambda item: item[1], reverse=True)
  #  return sorted_chars

def sorted_chars_dict(chars_dict):
    # Filter out non-alphabetic keys and sort by count in descending order
    # chars_dict.items() gives you (key, value) pairs
    # item[0] is the character (key), item[1] is the count (value)
    sorted_letters = sorted(
        [item for item in chars_dict.items() if isinstance(item[0], str) and item[0].isalpha()],
        key=lambda item: item[1],
        reverse=True
    )
    return sorted_letters

def report_format(path,total_words,sorted_caracters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for char,count in sorted_caracters:
        print(f"{char}: {count}")
    print("============= END ===============")

