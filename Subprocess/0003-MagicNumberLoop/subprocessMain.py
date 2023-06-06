# subprocessMain.py

import subprocess

magic_number_process = subprocess.run(["python", "magic_number.py"], capture_output=True, text=True)
magic_number_process.stdout
print(magic_number_process.stdout)


### OR ###

magic_number_process = subprocess.run(["python", "magic_number.py"], capture_output=True)
magic_number_process.stdout
print(magic_number_process.stdout.decode("UTF-8"))





# Start the magic_number.py script as a subprocess
magic_number_process = subprocess.Popen(["python", "-u", "magic_number.py"], stdout=subprocess.PIPE)
# magic_number_process.stdout
'''print(magic_number_process.stdout.read1().decode("utf-8"))
print("")
print(magic_number_process.stdout)
print("")
print(magic_number_process.poll())
print("")'''

# Read the output from the subprocess and print it in real-time
for line in iter(magic_number_process.stdout.readline, b''):
    print(line.decode('utf-8'), end='')

# Wait for the subprocess to finish
# magic_number_process.wait()



### OR ###

'''magic_number_process = subprocess.Popen(["python", "magic_number.py"], stdout=subprocess.PIPE)
magic_number_process.stdout
#print(magic_number_process.stdout.decode("UTF-8"))'''





### ADDING 2 RANDOM NUMBERS TOGETHER
'''print(sum(
    int(
        subprocess.run(["python", "magic_number.py"], capture_output=True).stdout
    )
    for _ in range(2)
))'''