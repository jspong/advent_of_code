#!/usr/local/bin/python3
import collections
import itertools
import math
import operator
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

def state_transition(state, line):
    if not line:
        return int(state) + 1
    return int(state)

def process_line(state, line, handle):
    original = line
    part = None
    if state == 0:
        part = []
        if not line.strip():
            return state_transition(state, original)
        num, line = line.split(':')
        for sub in line.strip().split('|'):
            sublist = []
            for token in sub.split():
                try:
                    sublist.append(int(token))
                except ValueError:
                    sublist.append(token[1:-1])
            part.append(sublist)
        part = [(int(num), part)]
    elif state == 1:
        part = line
    elif state == 2:
        pass
    elif state == 3:
        pass
    handle(part)
    return state_transition(state, original)

def to_regex(rules, rule):
    r = ''
    if isinstance(rule, int):
        return to_regex(rules, rules[rule])
    elif isinstance(rule, str):
        return rule

    if isinstance(rule[0], list):
        return '(' + '|'.join(to_regex(rules, r) for r in rule) + ')'
    else:
        for x in rule:
            if isinstance(x, str):
                r += x
            elif isinstance(x, list):
                r += to_regex(rules, rule)
            else:
                r += to_regex(rules, rules[x])

    return r

def solution(line, rules):
    r = to_regex(rules, rules[0]) + '$'
    return int(re.match(r, line) is not None)

def combine(results, rules):
    return sum(solution(line, rules) for line in results)

def main():
    state = 0
    parts = []
    mapping = {}
    rules = {}
    inputs = []
    with input_stream() as f:
        for line in f:
            line = line.strip()
            if state == 0:
                handler = rules.update
            else:
                handler = inputs.append
            state = process_line(state, line, handler)
    count = 0
    product = 1
    entries = []
    result = None

    if inputs:
        result = combine(inputs, rules)
    elif mapping:
        result = combine(mapping)

    return result

class Tests(unittest.TestCase):

    def test_self(self):
        self.assertEquals(solution(''), None)

if __name__ == '__main__':
    print(main())
