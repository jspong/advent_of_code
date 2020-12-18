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
    part = []
    kwargs = {}
    if state == 0:
        route, distance = line.split(' = ')
        source, destination = route.split(' to ')
        part = [(source, destination), (destination, source)]
        kwargs['weight'] = int(distance)
    elif state == 1:
        pass
    elif state == 2:
        pass
    elif state == 3:
        pass
    handle(part, **kwargs)
    return state_transition(state, original)

def stagger(iterable):
    first = True
    last = None
    for i, x in enumerate(iterable):
        if first:
            first = False
        else:
            yield (last, x)
        last = x

def solution(g):
    answer = None
    for source in g.nodes():
        for destination in g.nodes():
            if source == destination:
                continue
            paths = networkx.all_simple_paths(g, source, destination)
            for path in paths:
                if len(path) != len(g.nodes()):
                    continue
                distance = 0
                for a, b in stagger(path):
                    distance += g[a][b]['weight']
                if answer is None or distance < answer:
                    answer = distance
    return answer

def main():
    state = 0
    units = []
    mapping = {}
    g = networkx.DiGraph()
    with input_stream() as f:
        for line in f:
            line = line.strip()
            state = process_line(state, line, g.add_edges_from)
    count = 0
    product = 1

    answer = None
    if units:
        answer = sum(solution(u) for u in units)
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
