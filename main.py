def main():
    book_path = "books/frankenstein.txt"
    book_report(book_path)


def read_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def book_word_count(book_text):
    words = book_text.split()
    return len(words)

def book_character_count(book_text):
    character_count = {}
    for c in book_text:
        lower = c.lower()
        if lower in character_count.keys():
            character_count[lower] += 1
        else:
            character_count[lower] = 1
    return character_count


def get_book_name(book_path):
    book_name = book_path.replace('books/','')
    book_name = book_name.replace('.txt','')
    return book_name

def dict_to_dictlist(input_dict):
    output_list = []
    for c in input_dict:
        if c.isalpha():
            temp = {}
            temp[c] = input_dict[c]
            output_list.append(temp)
    return output_list

def sort_on(dict):
    for c in dict:
        return dict[c]

def print_dict_list(dict_list):
    for d in dict_list:
        for k in d:
            print(f"The '{k}' character was found {d[k]} times")

def book_report(book_path):
    book_name = get_book_name(book_path)
    print(f"--- Beign report of book: {book_name} at location: {book_path} ---")
    file_contents = read_book(book_path)
    book_text = read_book(book_path)
    word_count = book_word_count(book_text)
    print(f"word count in {book_name} is {word_count}")
    print("")
    character_count = book_character_count(book_text)
    dict_list = dict_to_dictlist(character_count)
    dict_list.sort(reverse=True, key=sort_on)
    print_dict_list(dict_list)

    print(f"--- End report ---")

main()
