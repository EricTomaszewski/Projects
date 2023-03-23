
import sys
import time

a = int(sys.argv[1])
b = int(sys.argv[2])

while a <= b:
    print(a)
    a += 1
    time.sleep(1)





'''import sys
import time

a = int(sys.argv[1])
b = int(sys.argv[2])

while True:
    time.sleep(1)
    a += 1
    b += 1
    print(f'{a}, {b}')
    sys.stdout.flush()'''





'''import sys
import time

# Read the input values from command line arguments
a = int(sys.argv[1])
b = int(sys.argv[2])

# Multiply the input values and print the output
for i in range(a,b+1):
    result = i
    time.sleep(0.5)
    print(result)
    sys.stdout.flush()'''
