def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)

main()

file_path = ("books/frankenstein/txt")

def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()  # Splits the text into words by whitespace
            word_count = len(words)
            print(f'Total number of words: {word_count}')
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
