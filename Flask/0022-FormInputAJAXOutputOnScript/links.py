'''import random
import time
import sys
    

def number_spit():
    try:
        # Read the input values from command line arguments
        current_number = sys.argv[1]
        while current_number < 100:
            current_number += 1
            print(current_number)
            sys.stdout.flush()                  # Flush stdout to make it immediately available in Flask
            time.sleep(1)
    except:
        pass'''



'''import random
import time
import sys

def number_spit():
    try:
        # Read the input values from command line arguments
        current_number = int(sys.argv[1])
        with open('output.txt', 'w') as f:
            while current_number < 100:
                current_number += 1
                print(current_number)
                sys.stdout.flush()  # Flush stdout to make it immediately available in Flask
                f.write(str(current_number) + '\n')
                f.flush()
                time.sleep(1)
    except:
        pass'''
        
        
import random
import time
import sys


def number_spit():
    try:
        # Read the input values from command line arguments
        current_number = int(sys.argv[1])
        while current_number < 100:
            current_number += 1
            print(current_number)
            sys.stdout.flush()  # Flush stdout to make it immediately available in Flask
            time.sleep(1)
    except:
        pass

