#!/usr/local/bin/python3
import sys
import operator

parts = []

def process_input_line(line):
    return [int(x) for x in line.split(',') if x != 'x']

if len(sys.argv) > 1:
    input_ = sys.argv[1]
else:
    input_ = "input.txt"

start, schedule, ids_ = 0, 0, 0
with open(sys.argv[1]) as f:
    start = int(f.readline())
    schedule = process_input_line(f.readline())

def solution():
    next_time = [((start // x + i) * x, x) for x in schedule for i in (0,1)]
    return min(((t, id_) for t, id_ in next_time if t >= start), key=operator.itemgetter(0))

x, y = solution()
print(x, y, (x-start) * y)
