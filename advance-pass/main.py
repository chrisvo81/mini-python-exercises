import random
import nltk

# Downloading the wordlist from nltk
nltk.download('words')
from nltk.corpus import words

# Lists for numbers and symbols
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def get_filtered_words(nr_words, word_length):
    filtered_words = [word for word in words.words() if len(word) == word_length]
    while len(filtered_words) < nr_words:
        print(f"Not enough words of length {word_length} available.")
        word_length = int(input("Enter a new length for the words:\n"))
        filtered_words = [word for word in words.words() if len(word) == word_length]
    return filtered_words

def generate_password(nr_words, word_length, nr_symbols, nr_numbers, generation_type):
    filtered_words = get_filtered_words(nr_words, word_length)
    password_parts = [random.choice(filtered_words) for _ in range(nr_words)] + \
                     [random.choice(symbols) for _ in range(nr_symbols)]

    if generation_type == 1:  # Extremely random
        password_parts += [random.choice(numbers) for _ in range(nr_numbers)]
        return ''.join(random.sample(password_parts, len(password_parts)))
    else:  # Randomized sections
        random.shuffle(password_parts)
        numbers_part = ''.join(random.choices(numbers, k=nr_numbers))
        return ''.join(password_parts) + numbers_part

def main():
    print("Welcome to the PyPassword Generator!")
    previous_settings = None

    while True:
        if previous_settings:
            use_previous = input("Do you want to use the same settings as before? (type 'y' to proceed): ").lower()
            if use_previous == "y":
                nr_words, word_length, nr_symbols, nr_numbers, generation_type = previous_settings
            else:
                previous_settings = None

        if not previous_settings:
            nr_words = int(input("How many words would you like in your password?\n"))
            word_length = int(input("What should be the length of each word?\n"))
            nr_symbols = int(input("How many symbols would you like?\n"))
            nr_numbers = int(input("How many numbers would you like?\n"))
            generation_type = int(input("Choose the password generation method (1 for Extremely Random, 2 for Randomized Sections):\n"))
            previous_settings = (nr_words, word_length, nr_symbols, nr_numbers, generation_type)

        password = generate_password(nr_words, word_length, nr_symbols, nr_numbers, generation_type)
        print(f"Generated Password: {password}")

        another = input("Do you want to generate another password? (type 'y' to proceed): ").lower()
        if another != "y":
            break

if __name__ == "__main__":
    main()
