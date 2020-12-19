#!/usr/local/bin/python3
import collections
import itertools
import math
import operator
import regex
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
    print(part)
    handle(part)
    return state_transition(state, original)

repeat = object()

step = ''
def to_regex(rules, index, rule, depth = 0):
    global step
    if depth == 0:
        step = ''
    r = ''
    if isinstance(rule, int):
        if rule == index:
            raise Exception
        return to_regex(rules, index, rules[rule], depth=depth+1)
    elif isinstance(rule, str):
        return rule
    elif isinstance(rule, list):
        if not rule:
            return ''
        if isinstance(rule[0], list):
            return '(?:' + '|'.join('(?:{})'.format(to_regex(rules, index, r, depth=depth+1)) for r in rule) + ')'
        else:
            for i, x in enumerate(rule):
                if isinstance(x, str):
                    r += x
                else:
                    if x == index:
                        remaining = to_regex(rules, index, rule[i+1:], depth=depth+1)
                        if remaining:
                            step += 'a'
                            return '(?P<c{}>((?:{})(?&c{})?(?:{})))'.format(step, r, step, remaining)

                        else:
                            return '(?:{})+'.format(r)
                    else:
                        r += to_regex(rules, x, rules[x], depth=depth+1)
    else:
        raise Exception(type(rule))

    return r

EXPECTED = [
"bbabbbbaabaabba",
"babbbbaabbbbbabbbbbbaabaaabaaa",
"aaabbbbbbaaaabaababaabababbabaaabbababababaaa",
"bbbbbbbaaaabbbbaaabbabaaa",
"bbbababbbbaaaaaaaabbababaaababaabab",
"ababaaaaaabaaab",
"ababaaaaabbbaba",
"baabbaaaabbaaaababbaababb",
"abbbbabbbbaaaababbbbbbaaaababb",
"aaaaabbaabaaaaababaa",
"aaaabbaabbaaaaaaabbbabbbaaabbaabaaa",
"aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"
]

def solution(line, rules):
    r = to_regex(rules, 0, rules[0]) + '$'
    print(r[2000:])
    result = int(regex.match(r, line) is not None)
    if result and line not in EXPECTED:
        print(line, result)
    return result

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
