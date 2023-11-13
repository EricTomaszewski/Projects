# python | subprocess module| subprocess.Popen| run OS command using subprocess
# https://www.youtube.com/watch?v=VlfLqG_qjx0

import subprocess

"""
The subprocess module allows you to spawn new processes.
Connect to their input/output/error pipes, and obtain their return codes.
e.g. df -h
subprocess.Popen
"""

cmd = "dir"

pl = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
out, err = pl.communicate()

print("out: {0}".format(out))
print("err: {0}".format(err))

if pl.returncode == 0:
    print("command: success")
else:
    print("command: failed")