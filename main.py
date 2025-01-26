file_path = 'books/frankenstein.txt'

def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split() 
            word_count = len(words)
            print(f'Total number of words: {word_count}')
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")

count_words_in_file(file_path)

