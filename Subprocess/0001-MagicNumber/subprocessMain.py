# subprocessMain.py

import subprocess

magic_number_process = subprocess.run(["python", "magic_number.py"], capture_output=True, text=True)
magic_number_process.stdout
print(magic_number_process.stdout)


### OR ###

magic_number_process = subprocess.run(["python", "magic_number.py"], capture_output=True)
magic_number_process.stdout
print(magic_number_process.stdout.decode("UTF-8"))




### ADDING 2 RANDOM NUMBERS TOGETHER
print(sum(
    int(
        subprocess.run(["python", "magic_number.py"], capture_output=True).stdout
    )
    for _ in range(2)
))