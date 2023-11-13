# run_examples.py

import subprocess

def print_output(process, name):
    print(f"\n{name} Output:")
    for line in iter(process.stdout.readline, b''):
        print(line, end='', flush=True)


# Run the script with buffered output
print("Running Buffered Example:")
buffered_process = subprocess.Popen(["python", "BuffUnbuff.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
print_output(buffered_process, "Buffered")

# Run the script with unbuffered output
print("\nRunning Unbuffered Example:")
unbuffered_process = subprocess.Popen(["python", "-u", "BuffUnbuff.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
print_output(unbuffered_process, "Unbuffered")

# Wait for both processes to finish
buffered_process.wait()
unbuffered_process.wait()
