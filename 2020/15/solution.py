#!/usr/local/bin/python3
import itertools
import collections
import sys

parts = []

def process_input_line(line):
    return int(line)

if len(sys.argv) > 1:
    input_ = sys.argv[1]
else:
    input_ = "input.txt"

with open(sys.argv[1]) as f:
    parts = [int(i) for i in f.read().strip().split(',')]

NUM = 30000000
STEP = 100000
def solution():
    history = collections.defaultdict(list)
    last = None
    i = 0
    while i < NUM:
        this = last
        if i < len(parts):
            last = parts[i]
            if i != len(parts)-1:
                history[last].append(i)
                #print('[{}].append({})'.format(last, i))
        else:
            if last in history:
                next_ = i - history[last][-1] - 1
                #print('[{}].append({})'.format(last, i-1))
                history[last].append(i-1)
                last = next_
            else:
                history[last].append(i-1)
                #print('[{}].append({})'.format(last, i-1))
                last = 0
        i += 1
        if i % STEP == 0:
            print("{:10d}\n{:10d}".format(i, NUM))
    return last



print(solution())
