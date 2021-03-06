#!/usr/local/bin/python3
import itertools
import collections
import os
import re
import networkx
import pygraphviz
from networkx.drawing.nx_agraph import write_dot
import string
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

def validate_password(password):
    for i, _ in enumerate(string.ascii_lowercase[:-2]):
        if (string.ascii_lowercase[i] + string.ascii_lowercase[i+1] + string.ascii_lowercase[i+2]) in password:
            break
    else:
        return 1
    if any(l in password for l in 'iol'):
        return 2
    overlaps = 0
    for letter in string.ascii_lowercase:
        if letter + letter in password:
            overlaps += 1
    return 0 if overlaps >= 2 else 3

def next_password(password):
    if any(l in password for l in 'iol'):
        first = min(x if x >= 0 else len(password)-1 for x in (password.find('i'), password.find('o'), password.find('l')))
        new = password[:first+1] + ('z' * (len(password) - first-1))
        password = new
    return ''.join(string.ascii_lowercase[i] for i in next_indices(password))

def next_indices(password):
    carry = 1
    indices = []
    rev = ''.join(reversed(password))
    num = len(string.ascii_lowercase)
    for c in rev:
        i = string.ascii_lowercase.index(c)
        step = i + carry
        if step >= num:
            indices.append(step % num)
            carry = 1
        else:
            indices.append(step)
            carry = 0
    return reversed(indices)


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
    line = next_password(line)
    c = collections.Counter()
    while  validate_password(line):
        c[validate_password(line)] += 1
        line = next_password(line)
    print(c)
    return line

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
        answer = solution(units[0])
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

    if not validate_password(answer):
        return answer
    else:
        raise Exception(answer)

class Tests(unittest.TestCase):

    def test_next(self):
        self.assertEqual(next_password('hxbxwxba'), 'hxbxwxbb')
        self.assertEqual(next_password('hxbxwxzz'), 'hxbxwyaa')
        self.assertEqual(next_password('hxbiwxzz'), 'hxbjaaaa')

    def test_self(self):
        self.assertFalse(not validate_password('hijklmmn'))
        self.assertFalse(not validate_password('abbceffg'))
        self.assertFalse(not validate_password('abbcegjk'))
        self.assertTrue(not validate_password('abcdffaa'))
        self.assertTrue(not validate_password('ghjaabcc'))

    def test_solution(self):
        self.assertEqual(solution('abcdefgh'), 'abcdffaa')
        self.assertEqual(solution('ghijklmn'), 'ghjaabcc')


if __name__ == '__main__':
    print(main())
