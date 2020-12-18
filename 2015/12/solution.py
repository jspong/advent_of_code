#!/usr/local/bin/python3
import itertools
import collections
import json
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

def solution(j):
    if isinstance(j, list):
        return sum(solution(x) for x in j)
    elif isinstance(j, dict):
        count = 0
        for k,v in j.items():
            try:
                count += int(k)
            except:
                pass
            count += solution(v)
        return count
    elif isinstance(j, int):
        return j
    else:
        return 0

def main():
    state = 0
    units = []
    mapping = {}
    g = networkx.DiGraph()
    with input_stream() as f:
        s = f.read()
        print(repr(s))
        j = json.loads(s)
    return solution(j)
    count = 0
    product = 1
    for part in parts:
        pass

    answer = None
    if units:
        answer = sum(solution(u) for u in unites)
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

    return answer

class Tests(unittest.TestCase):

    def test_self(self):
        self.assertEquals(solution(''), None)

if __name__ == '__main__':
    print(main())
