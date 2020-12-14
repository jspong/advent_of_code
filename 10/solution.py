#!/usr/local/bin/python3
import sys

parts = []

def process_input_line(line):
    return int(line)

if len(sys.argv) > 1:
    input_ = sys.argv[1]
else:
    input_ = "input.txt"

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        part = process_input_line(line)
        parts.append(part)

checked = set()

cache = {}
def solution():
    adapters = list(sorted(set(parts)))
    print(2 ** len(adapters))
    adapters.append(adapters[-1] + 3)

    def sub(current, adapters):
        key = tuple([current] + adapters)
        if key in cache:
            return cache[key]
        if not adapters:
            return 1
        options = list(valid(current, adapters))
        count = 0
        for i, option in enumerate(options):
            count += sub(option, adapters[i+1:])
        cache[key] = count
        return count

    return sub(0, adapters)

def valid(current, adapters):
    for part in adapters:
        if part - current in (1,2,3):
            yield part
        else:
            break

print(solution())
