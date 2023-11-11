# MULTIPLE TESTS TO UNDERSTAND SUBPROCESS MODULE
# https://www.youtube.com/watch?v=2Fp1N6dof0Y



import subprocess

# subprocess.run('dir')         # does NOT work on Windows unless shell=True
# subprocess.run('dir', shell=True)

pl = subprocess.run('dir', shell=True)                          # capturing output IN the console
print(pl.returncode)                                            # code 0 for no errors
# print(pl)

print("")

pl = subprocess.run('dir', shell=True, capture_output=True)     # capturing output INSTEAD of console
# print(pl.stdout)                                              # bytes output
print(pl.stdout.decode())                                       # bytes converted into string

print("")

pl = subprocess.run('dir', shell=True, capture_output=True, text=True)     # capturing output INSTEAD of console
print(pl.stdout)                                                # bytes output automatically converted into string through text=True

print("")

# the same as above example
pl = subprocess.run('dir', shell=True, stdout=subprocess.PIPE, text=True)     # capturing output INSTEAD of console
print(pl.stdout)                                                # bytes output automatically converted into string through text=True

print("")

with open('output.txt', 'w') as f:
    pl = subprocess.run('dir', shell=True, stdout=f, text=True)     # redirecting to file
    
print("")

# capturing the dne folder which does NOT exist
pl = subprocess.run(['dir', 'dne'], shell=True, capture_output=True, text=True)     # capturing output INSTEAD of console
print(pl.returncode)                                                # now the code is 1 because there is an error (directory 'dne' does not exist)
print(pl.stderr)                                                    # it returns the message of an error (rather than the code of it)
#  if pl.returncode==0 is the same as pl = subprocess.run(['dir', 'dne'], shell=True, capture_output=True, text=True, check=True) 

print("")

# capturing the dne folder which does NOT exist
pl = subprocess.run(['dir', 'dne'], shell=True, stderr=subprocess.DEVNULL)     # redirecting the error name to NULL
print(pl.returncode)                                                # now the code is 1 because there is an error (directory 'dne' does not exist)
print(pl.stderr)                                                    # it returns the message of an error (rather than the code of it)

print("")

# opening text.txt file
pl = subprocess.run(['type', 'text.txt'], shell=True, capture_output=True, text=True)     # 
print(pl.stdout)                                                    # now the code is 1 because there is an error (directory 'dne' does not exist)

print("")

# opening text.txt file & searching for a text string within it
pl = subprocess.run(['type', 'text.txt'], shell=True, capture_output=True, text=True)     # 
# print(pl.stdout)                                                    # now the code is 1 because there is an error (directory 'dne' does not exist)
p2 = subprocess.run(['findstr', '/n', 'test'], capture_output=True, text=True, input=pl.stdout)     # input is the read from pl output
print(p2.stdout)

print("")

# THE SAME AS ABOVE BUT WITHOUT [] FOR THE MAIN COMMAND >>> opening text.txt file & searching for a text string within it
pl = subprocess.run('type text.txt', shell=True, capture_output=True, text=True)     # 
# print(pl.stdout)                                                    # now the code is 1 because there is an error (directory 'dne' does not exist)
p2 = subprocess.run(['findstr', '/n', 'test'], capture_output=True, text=True, input=pl.stdout)     # input is the read from pl output
print(p2.stdout)

print("")

# THE SAME AS ABOVE BUT WITHOUT [] FOR THE MAIN COMMAND & IN A SINGLE LINE>>> opening text.txt file & searching for a text string within it
pl = subprocess.run('type text.txt | findstr /n test', shell=True, capture_output=True, text=True)     # 
print(pl.stdout)                                                    # now the code is 1 because there is an error (directory 'dne' does not exist)