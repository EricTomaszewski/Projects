import subprocess

def run_script():
    process = subprocess.Popen(['python', '-u', 'random_generator.py'], stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
    for line in process.stdout:
        print(line, end='')
    # Iterate over each character in the line
'''    for line in process.stdout:
        for char in line.strip():  # Iterate over each character in the line
            print(char)'''

run_script()