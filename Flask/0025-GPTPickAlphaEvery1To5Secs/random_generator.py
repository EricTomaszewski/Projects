import random
import string
import time

""" def generate_random_value():
    while True:
        value = ''.join(random.choices(string.ascii_letters + string.digits, k=1))
        print(value)
        time.sleep(random.randint(5, 10)) """



def generate_random_word():
    length = random.randint(1, 10)  # Random word length between 1 and 10
    word = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return word

def generate_random_words(num_words):
    words = []
    for _ in range(num_words):
        word = generate_random_word()
        words.append(word)
    return words

num_words = 3  # Number of random words to generate


def generate_random_value():
    while True:
        value = generate_random_words(num_words)
        value = ' '.join(value)
        print(value)
        time.sleep(random.randint(5, 10))


# generate_random_value()

if __name__ == '__main__':
    generate_random_value()
    
    
