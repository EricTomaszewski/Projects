    
    
# buffered_example.py

import time


print("Buffered Example:")
for i in range(5):
    print(f"Line {i}")
    time.sleep(1)


"""print("\nUnbuffered Example:")
for i in range(5):
    print(f"Line {i}", flush=True)
    time.sleep(1)
"""