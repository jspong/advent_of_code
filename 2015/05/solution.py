#!/usr/local/bin/python3
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
        part = line
    elif state == 1:
        pass
    elif state == 2:
        pass
    elif state == 3:
        pass
    handle(part)
    return state_transition(state, original)

def has_two_doubles(line):
    for i in range(0, len(line)-1):
        start, end = i, i+2
        double = line[start:end]
        if double in line[:start] or double in line[end:]:
            return True
    return False

def solution(line):
    if not has_two_doubles(line):
        return False
    return bool(re.search(r'(\w)\w\1', line))

def main():
    state = 0
    parts = []
    with input_stream() as f:
        for line in f:
            line = line.strip()
            state = process_line(state, line, parts.append)
    count = 0
    product = 1
    for part in parts:
        count += solution(part)
    return count

class Tests(unittest.TestCase):

    def test_self(self):
        self.assertTrue(solution('qjhvhtzxzqqjkmpb'))
        self.assertTrue(solution('xxyxx'))
        self.assertFalse(solution('uurcxstgmygtbstg'))
        self.assertFalse(solution('ieodomkazucvgmuy'))

if __name__ == '__main__':
    print(main())
