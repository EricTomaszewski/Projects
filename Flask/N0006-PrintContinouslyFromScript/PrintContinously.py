'''a = int(input("First number:        "))
b = int(input("Second number:       "))

print(f"The sum of your numbers is:   ", a + b)
'''


import sys
import time

# Read the input values from command line arguments
a = int(sys.argv[1])
b = int(sys.argv[2])

# Multiply the input values and print the output
for i in range(a,b+1):
    result = i
    time.sleep(0.5)
    print(result)
