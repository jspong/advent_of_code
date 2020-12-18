#!/usr/local/bin/python3
import itertools
import collections
import re
import networkx
import os
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
    delims = 2
    i = 0
    for c in line:
        if c in '\\"':
            delims += 1
    return delims

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

    if os.environ.get('DEBUG'):
        print(state)
        for unit in units:
            print(units)
        for k, v in mapping.items():
            print(k, v)
        if g.nodes():
            write_dot(g, sys.stdout)
    return sum(solution(u) for u in units)

class Tests(unittest.TestCase):

    def test_self(self):
        self.assertEquals(solution('""'), 2)
        self.assertEquals(solution('"abc"'), 2)
        self.assertEquals(solution('"aaa\\"aaa"'), 3)
        self.assertEquals(solution('\\x27'), 5)

if __name__ == '__main__':
    print(main())
