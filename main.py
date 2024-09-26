def word_counter (text):
    return(len(text.split()))

def character_counter (text):
    characters_dict = {}
    lowered_text = text.lower()
    letters = list(lowered_text)
    for char in letters:
        if char not in characters_dict:
            characters_dict[char] = 1
        else:
            characters_dict[char] += 1
    return characters_dict

def get_amount(dict_item):
    return dict_item['amount']

def sort_on (characters_dict):
    letters_list = []
    for letter, amount in characters_dict.items():
        if letter.isalpha():
            letters_list.append({"letter":letter, "amount":amount})
    letters_list.sort(reverse=True, key=get_amount)
    return letters_list

def main():
    with open("books/frankenstein.txt") as f:
            file_contents = f.read()
    return file_contents    

if __name__ == "__main__":
    text = main()
    char_dict = character_counter(text)
    
    


