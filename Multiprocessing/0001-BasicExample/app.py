import multiprocessing as mp
import time
import math


results_1 = []
results_2 = []
results_3 = []


def make_calculation_1(numbers):
    for number in numbers:
        results_1.append(math.sqrt(number ** 3))
        
def make_calculation_2(numbers):
    for number in numbers:
        results_2.append(math.sqrt(number ** 4))
        
def make_calculation_3(numbers):
    for number in numbers:
        results_3.append(math.sqrt(number ** 5))
        
        
numbers_list = list(range(5000000))


if __name__ == "__main__":              # with MULTIprocessing => it is a must have
    # MULTIPROCESSING => parallel calculations
    p1 = mp.Process(target=make_calculation_1, args=(numbers_list,))
    p2 = mp.Process(target=make_calculation_2, args=(numbers_list,))
    p3 = mp.Process(target=make_calculation_3, args=(numbers_list,))
    
    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    end = time.time()
    print(f"Multiprocessing time:    {end-start:.2f}")
    print("")
    
    # NOT parallel => linear
    start = time.time()
    make_calculation_1(numbers_list)
    make_calculation_2(numbers_list)
    make_calculation_3(numbers_list)                       
    end = time.time()
    print("Linear processing time: ", "{:.2f}".format(end-start))
    print("")
    print("")
    
    print("'Games' with formatting of print")
    print("Linear processing time:", end-start, "  >>> integer")
    print("Linear processing time: " +  str(end-start) + "   >>> string")
    print("Linear processing time: ", "{:.2f}".format(end-start), "   >>> format()")
    print(f"Linear processing time:  {end-start:.2f}    >>> f-string")