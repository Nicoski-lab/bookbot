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

def main():
    with open("books/frankenstein.txt") as f:
            file_contents = f.read()
    return file_contents    

if __name__ == "__main__":
    text = main()
    char_count = character_counter(text)
    print('The book has',word_counter(text),'words.')
    print (char_count)


