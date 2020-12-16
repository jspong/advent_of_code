#!/usr/local/bin/python3
import itertools
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

def process_line(state, line, handle, state_transition=lambda x, line: x):
    original = line
    part = None
    if state == 0:
        if line.startswith('turn '):
            action, rest = line[5:].split(' ', 1)
            action = 1 if action == 'on' else -1
        else:
            rest = line[len('toggle '):]
            action = 2
        def parse(section):
            to, from_ = section.split(' through ')
            a = to.split(',')
            b = from_.split(',')
            return ((int(a[0]),int(a[1])), (int(b[0]), int(b[1])))
        part = action, parse(rest)
        print(part)

    elif state == 1:
        pass
    elif state == 2:
        pass
    elif state == 3:
        pass
    handle(part)
    return state_transition(state, original)

def solution(line):
    pass

def main():
    state = 0
    parts = []
    with input_stream() as f:
        for line in f:
            line = line.strip()
            state = process_line(state, line, parts.append)
    count = 0
    product = 1
    board = [[0 for _ in range(1000)] for _ in range(1000)]
    for part in parts:
        action, to_from = part
        from_, to = to_from
        for x in range(from_[0], to[0]+1):
            for y in range(from_[1], to[1]+1):
                board[x][y] = max(0, board[x][y] + action)
    for row in board:
        for cell in row:
            count += cell
    return count

class Tests(unittest.TestCase):

    def test_self(self):
        self.assertEquals(solution(''), None)

if __name__ == '__main__':
    print(main())
