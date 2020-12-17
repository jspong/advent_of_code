#!/usr/local/bin/python3
import collections
import itertools
import operator
import re
import sys
import unittest

def input_stream():
    if len(sys.argv) > 1:
        if sys.argv[1] == '-':
            return sys.stdin
        else:
            return open(sys.argv[1])
    else:
        return open('input.txt')

states = list(range(10))

def state_transition(state, line):
    return state

def process_line(state, i, line, handle):
    original = line
    part = []
    if state == 0:
        for x, c in enumerate(line):
            if c == '#':
                part.append(((i, x, 0), 1))
    elif state == 1:
        pass
    elif state == 2:
        pass
    elif state == 3:
        pass
    handle(part)
    return state_transition(state, original)

def main():
    state = 0
    positions = collections.defaultdict(int)
    with input_stream() as f:
        num_lines = 0
        for i, line in enumerate(f):
            num_lines += 1
            line = line.strip()
            state = process_line(state, i, line, positions.update)
    count = 0
    product = 1
    entries = []
    x = 0, max(p[1] for p in positions) + 1
    y = 0, num_lines
    z = 0, 1
    for n in range(6):
        x = x[0] - 1, x[1] + 1
        y = y[0] - 1, y[1] + 1
        z = z[0] - 1, z[1] + 1
        new_positions = collections.defaultdict(int)
        for i in range(*x):
            for j in range(*y):
                for k in range(*z):
                    new_positions[(i,j,k)] = step(positions, i, j, k)
        positions = new_positions

    return sum(positions.values())

def dump(positions, x, y, z):
    for k in range(*z):
        print("z={}".format(k))
        for i in range(*x):
            for j in range(*y):
                print('#' if positions[(i, j, k)] else '.', end='')
            print()

def step(positions, x, y, z):
    if positions[(x,y,z)]:
        return int(neighbors(positions, x, y, z) in (2, 3))
    else:
        return int(neighbors(positions, x, y, z) == 3)

def neighbors(positions, x, y, z):
    count = 0
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            for k in (-1, 0, 1):
                if i == 0 and j == 0 and k == 0:
                    continue
                count += positions[(x+i, y+j, z+k)]
    return count


class Tests(unittest.TestCase):

    def test_self(self):
        self.assertEquals(solution(''), None)

if __name__ == '__main__':
    print(main())
