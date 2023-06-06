# reaction_game.py

from time import perf_counter, sleep
from random import random

print("Press enter to play")
input()
print("OK. Get ready!")
sleep(random() * 5 + 1)
print("Go!")
start = perf_counter()
input()
end = perf_counter()
print(f"You reacted in {(end-start) * 1000:.0f} miliseconds!\nGoodbye!")