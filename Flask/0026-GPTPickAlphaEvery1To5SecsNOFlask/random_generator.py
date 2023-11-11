'''import random
import string
import time

def generate_random_value():
    while True:
        value = ''.join(random.choices(string.ascii_letters + string.digits, k=1))
        print(value)
        time.sleep(random.randint(1, 5))

generate_random_value()'''



import random
import string
import time

def generate_random_value():
    while True:
        length = random.randint(1, 10)  # Generate a random length from 1 to 10
        value = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        print(value)
        time.sleep(random.randint(1, 5))

generate_random_value()
