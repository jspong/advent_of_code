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

def solution():
    bits = {}
    mask = ''
    for part in parts:
        if part[0] == 'MASK':
            mask = part[1]
        else:
            location, value = part[1:]
            print(value)
            print("M: {}".format(mask))
            print("I: {0:036b}".format(value))

            for i, m in enumerate(mask):
                place = 2 ** (len(mask) - 1 - i)
                bit = value & place
                if m == '1':
                    value |= place
                elif m == '0':
                    if value & place:
                        value -= place
            bits[part[1]] = value
            print("O: {0:036b}".format(value))
    return sum(bits.values())

#print(parts)
print(solution())
