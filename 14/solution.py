#!/usr/local/bin/python3
import sys

parts = []

def process_input_line(line):
    if line.startswith('mask'):
        return 'MASK', line.split()[2]
    elif line.startswith('mem'):
        return 'MEM', int(line[4:line.index(']')]), int(line.split()[2])
        line = line[:line.indexof(']')]
    else:
        raise Exception(line)


if len(sys.argv) > 1:
    input_ = sys.argv[1]
else:
    input_ = "input.txt"

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        part = process_input_line(line)
        parts.append(part)

def possibilities(mask, number):
    if len(mask) == 0 or all(m == '0' for m in mask):
        yield number
        return
    for i, m in enumerate(mask):
        place = 2 ** (len(mask) - 1 - i)
        if m == '1':
            for possibility in possibilities(mask[i+1:], number | place):
                yield possibility
            break
        elif m == 'X':
            for possibility in possibilities(mask[i+1:], number | place):
                yield possibility
            for possibility in possibilities(mask[i+1:], number & ~place):
                yield possibility
            break

def solution():
    bits = {}
    mask = ''
    for part in parts:
        if part[0] == 'MASK':
            mask = part[1]
        else:
            location, value = part[1:]
            choices = set(possibilities(mask, location))
            for choice in choices:
                bits[choice] = value
    print(bits)
    print(sorted(bits.keys()))
    return sum(bits.values())

#print(parts)
print(solution())
