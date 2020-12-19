#!/usr/local/bin/python3
import collections
import itertools
import math
import operator
import os
import re
import networkx
import sys
import unittest

import pygraphviz
from networkx.drawing.nx_agraph import write_dot

def process_line(state, line, handle):
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
    return 0

def combine(results):
    return sum(solution(r) for r in results)

def state_transition(state, line):
    return state

class Tests(unittest.TestCase):

    def test_self(self):
        self.assertEquals(solution(''), None)

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
        write_dot(g, sys.stdout)
        result = combine(g)
    elif dg.edges():
        write_dot(dg, sys.stdout)
        result = combine(dg)

    return result

def input_stream():
    if len(sys.argv) > 1:
        if sys.argv[1] == '-':
            return sys.stdin
        else:
            return open(sys.argv[1])
    else:
        return open('input.txt')

if __name__ == '__main__':
    print(main())
