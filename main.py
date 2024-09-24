def words_counter (text):
    return(len(text.split()))

def main():
    with open("books/frankenstein.txt") as f:
            file_contents = f.read()
    return file_contents    

if __name__ == "__main__":
    text = main()
    print('The book has',words_counter(text),'words.')


