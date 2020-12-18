#!/usr/local/bin/python3
import itertools
import collections
import re
import os
import networkx
import pygraphviz
from networkx.drawing.nx_agraph import write_dot
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

def process_line(state, line, handle, state_transition=lambda x, line: x):
    original = line
    part = None
    if state == 0:
        part = line
    elif state == 1:
        pass
    elif state == 2:
        pass
    elif state == 3:
        pass
    handle(part)
    return state_transition(state, original)

def solution(line):
    solution = ''
    while line:
        i, j = 0, 1
        while j < len(line) and line[j] == line[i]:
            j += 1
        solution += '{}{}'.format(j-i, line[i])
        line = line[j:]
    return solution


def main():
    state = 0
    units = []
    mapping = {}
    g = networkx.DiGraph()
    with input_stream() as f:
        for line in f:
            line = line.strip()
            state = process_line(state, line, units.append)
    count = 0
    product = 1

    answer = None
    if units:
        answer = [solution(u) for u in units]
        for line in answer:
            print(line)
    elif mapping:
        answer = solution(mapping)
    elif g:
        answer = solution(g)
    else:
        raise Exception()

    if os.environ.get('DEBUG'):
        print(state)
        for unit in units:
            print(units)
        for k, v in mapping.items():
            print(k, v)
        if g.nodes():
            write_dot(g, sys.stdout)

    x = units[0]
    for _ in range(50):
        x = solution(x)
    return len(x)

class Tests(unittest.TestCase):

    def test_self(self):
        self.assertEquals(solution(''), None)

if __name__ == '__main__':
    print(main())
