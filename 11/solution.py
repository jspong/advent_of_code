#!/usr/local/bin/python3
import sys

parts = []

def process_input_line(line):
    return line

if len(sys.argv) > 1:
    input_ = sys.argv[1]
else:
    input_ = "input.txt"

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        part = process_input_line
        parts.append(line)

def solution():
    pass

print(solution())
