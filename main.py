def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    number_of_words = get_number_of_words(text)
    letter_count = get_letter_count(text)
    printable_list = cast_to_sorted_list(letter_count)
    printable_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document")
    print("")
    for element in printable_list:
        print(f"The '{element["letter"]}' character was found {element["count"]} times")
    print("--- End report ---")

def get_text(path):
    with open(path) as f:
        return f.read()
    
def get_number_of_words(text):
    return len(text.split())

def get_letter_count(text):
    letter_dictionary = {}
    for letter in text:
        lowecase_letter = letter.lower()
        if lowecase_letter in letter_dictionary:
            letter_dictionary[lowecase_letter] += 1
        else:
            letter_dictionary[lowecase_letter] = 1
    
    return letter_dictionary

def cast_to_sorted_list(dict):
    result = []
    for key in dict:
        if key.isalpha():
            new_dict = {"letter": key, "count": dict[key]}
            result.append(new_dict)
    return result

def sort_on(dict):
    return dict["count"]


main()