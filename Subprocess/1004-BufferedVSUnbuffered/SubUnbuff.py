# run_examples.py

import subprocess

# Run the script with buffered output
"""print("Running Buffered Example:")
buffered_process = subprocess.Popen(["python", "BuffUnbuff.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
buffered_stdout, buffered_stderr = buffered_process.communicate()
print("Buffered Output:")
print(buffered_stdout.decode('utf-8'))"""

# Run the script with unbuffered output
print("\nRunning Unbuffered Example:")
unbuffered_process = subprocess.Popen(["python", "-u", "BuffUnbuff.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
unbuffered_stdout, unbuffered_stderr = unbuffered_process.communicate()
print("Unbuffered Output:")
print(unbuffered_stdout.decode('utf-8'))
