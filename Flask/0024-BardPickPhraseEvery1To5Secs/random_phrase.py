import random
import time

def get_random_phrase():
  phrases = ["abc", "def", "ghi", "jkl", "mno"]
  return random.choice(phrases)

def main():
  while True:
    phrase = get_random_phrase()
    print(phrase)
    time.sleep(random.randint(1, 5))

if __name__ == "__main__":
  main()
