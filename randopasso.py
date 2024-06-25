import random

def read_special_characters(file_path):
    with open(file_path, 'r') as file:
        special_chars = file.read().splitlines()
    return special_chars

def read_random_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
    return words

def generate_password(words, special_chars, num_words=1, num_special=2, num_digits=2):
    selected_words = random.sample(words, num_words)
    selected_special_chars = random.choices(special_chars, k=num_special)
    selected_digits = [str(random.randint(0, 9)) for _ in range(num_digits)]

    password_list = selected_words + selected_special_chars + selected_digits
    random.shuffle(password_list)

    password = ''.join(password_list)
    return password

special_chars_file_path = '/Users/scottyh/Desktop/till i get a new idea/special_characters.txt'
random_words_file_path = '/Users/scottyh/Library/Mobile Documents/com~apple~TextEdit/Documents/500-Random-Words.rtf'

special_chars = read_special_characters(special_chars_file_path)
random_words = read_random_words(random_words_file_path)

password = generate_password(random_words, special_chars)

print("Your Password", password)