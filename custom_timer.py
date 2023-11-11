# TIMER MODULE

import timeit

def custom_timer(number, repeat):
    def wrapper(func):
        runs = timeit.repeat(func, number=number, repeat=repeat)
        print(sum(runs) / len(runs))
        
    return wrapper