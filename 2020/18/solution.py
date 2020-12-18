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
    while '(' in line:
        last = -1
        line = re.sub(r'\s*\(\s*', ' ( ', line)
        line = re.sub(r'\s*\)\s*', ' ) ', line)
        line = re.sub('[+]', ' + ', line)
        line = re.sub('[*]', ' * ', line)
        line = re.sub('\s+', ' ', line)
        line = line.strip()
        for i, c in enumerate(line):
            if c == '(':
                last = i
            elif c == ')':
                sub = line[last+1:i-1].strip()
                line = line[:last] + '{}'.format(solution(sub)) + line[i+1:]
                break
    current = None
    operator = None
    parts = line.split()

    while '+' in parts:
        plus = parts.index('+')
        a, b = plus-1, plus+1
        parts = parts[:a] + [int(parts[a]) + int(parts[b])] + parts[b+1:]

    while '*' in parts:
        plus = parts.index('*')
        a, b = plus-1, plus+1
        parts = parts[:a] + [int(parts[a]) * int(parts[b])] + parts[b+1:]

    return parts[0]

def main():
    state = 0
    parts = []
    with input_stream() as f:
        for line in f:
            line = line.strip()
            state = process_line(state, line, parts.append)
    count = 0
    product = 1
    entries = []
    for part in parts:
        count += solution(part)
    return count

class Tests(unittest.TestCase):

    def test_self(self):
        self.assertEqual(solution('1 + (2 * 3) + (4 * (5 + 6))'), 51)
        self.assertEqual(solution('2 * 3 + (4 * 5)'), 46)
        self.assertEqual(solution('5 + (8 * 3 + 9 + 3 * 4 * 3)'), 1445)
        self.assertEqual(solution('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'), 669060)
        self.assertEqual(solution('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'), 23340)

if __name__ == '__main__':
    print(main())
