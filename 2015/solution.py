#!/usr/local/bin/python3
import collections
import itertools
import re
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
    return

def combine(results):
    if not results:
        return None
    value = type(results[0])()
    for result in results:
        value += result
    return value

def main():
    state = 0
    parts = []
    mapping = {}
    g = networkx.Graph()
    dg = networkx.DiGraph()
    with input_stream() as f:
        for line in f:
            line = line.strip()
            state = process_line(state, line, parts.append)
    count = 0
    product = 1
    entries = []
    result = None

    if parts:
        result = combine(parts)
    elif mapping:
        result = combine(mapping)
    elif g.edges():
        result = combine(g)
    elif dg.edges():
        result = combine(dg)

    return result

class Tests(unittest.TestCase):

    def test_self(self):
        self.assertEquals(solution(''), None)

if __name__ == '__main__':
    print(main())
