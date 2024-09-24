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

def sort_on (characters_dict):
    letters = [
        {"letter":"test1", "number": 5},
        {"letter":"test2", "number": 1},
        {"letter":"test3", "number": 10}
    ]        
    #letters.sort(reverse=True, key=sort_on)
    return letters

def main():
    with open("books/frankenstein.txt") as f:
            file_contents = f.read()
    return file_contents    

if __name__ == "__main__":
    text = main()
    char_dict = character_counter(text)
    report = sort_on(char_dict)
    print('The book has',word_counter(text),'words.')
    print(report)


