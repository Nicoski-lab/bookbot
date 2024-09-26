def word_counter(text):
    return len(text.split())

def character_counter(text):
    characters_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char.isalpha():
            characters_dict[char] = characters_dict.get(char, 0) + 1
    return characters_dict

def get_amount(dict_item):
    return dict_item['amount']

def sort_characters(characters_dict):
    letters_list = [{"letter": letter, "amount": amount} 
                    for letter, amount in characters_dict.items()]
    letters_list.sort(reverse=True, key=get_amount)
    return letters_list

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents    

if __name__ == "__main__":
    text = main()
    char_dict = character_counter(text)
    word_count = word_counter(text)
    sorted_chars = sort_characters(char_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    for char_info in sorted_chars:
        print(f"The '{char_info['letter']}' character was found {char_info['amount']} times")

    print("--- End report ---")