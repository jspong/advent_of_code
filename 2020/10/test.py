#!/usr/local/bin/python3

import os
import subprocess
import sys

current = sys.argv[1]
next_ = "test" + str(int(current[4:-4]) + 1) + ".txt"

proc = subprocess.Popen(['/usr/local/bin/python3', 'solution.py', current], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

rc = proc.wait()

if rc:
    print(proc.stderr.read())

contents = proc.stdout.read().decode()
print("STDOUT from solution.py: \n{}".format(contents))

if os.path.exists(next_):
    with open(next_) as f:
        next_contents = f.read()
    if '\n'.join(contents.strip().splitlines()[:-1]) == next_contents.strip():
        print("contents match " + next_)
    else:
        print("contents do not match " + next_)
else:
    print("no file " + next_ + " to compare to")

