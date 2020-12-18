#!/usr/local/bin/python3
import networkx
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
    kwargs = {}
    if state == 0:
        command, _, target = line.partition(' -> ')
        if ' ' in command:
            if command.startswith('NOT '):
                part = [(command[4:], target)]
                kwargs['action'] = 'NOT'
            else:
                a, operand, b = command.split(' ')
                mid = '{}_{}_{}'.format(a,operand,b)
                part = [(a, mid), (b, mid), (mid, target)]
                kwargs['action'] = operand
        else:
            part = [(command, target)]
    elif state == 1:
        pass
    elif state == 2:
        pass
    elif state == 3:
        pass
    handle(part, **kwargs)
    return state_transition(state, original)

def solution(head, g, values):
    edges = list(g.in_edges({head}, data=True))
    if not edges:
        return int(head)
    if head in values:
        return values[head]
    action = edges[0][2].get('action')
    if len(edges) == 1:
        a, b = edges[0][0], None
    elif len(edges) == 2:
        a, b = edges[0][0], edges[1][0]
    else:
        raise Exception(edges)
    value = None
    if action is None:
        value = solution(a, g, values)
    elif action == 'NOT':
        value = ~solution(a, g, values)
    elif action == 'LSHIFT':
        if b is None:
            value = solution(a, g, values)
        else:
            value = solution(a, g, values) << solution(b, g, values)
    elif action == 'RSHIFT':
        if b is None:
            value = solution(a, g, values)
        else:
            value = solution(a, g, values) >> solution(b, g, values)
    elif action == 'AND':
        if b is None:
            value = solution(a, g, values)
        else:
            value = solution(a, g, values) & solution(b, g, values)
    elif action == 'OR':
        if b is None:
            value = solution(a, g, values)
        else:
            value = solution(a, g, values) | solution(b, g, values)
    else:
        raise Exception(action)

    if value < 0:
        value = value % 65535 + 1
    values[head] = value
    return value

def main():
    state = 0
    parts = []
    g = networkx.DiGraph()
    with input_stream() as f:
        for line in f:
            line = line.strip()
            state = process_line(state, line, g.add_edges_from)
    count = 0
    product = 1
    state = {}
    head = None
    states = {}
    solution('a', g, states)
    return states['a']

class Tests(unittest.TestCase):

    def test_self(self):
        self.assertEquals(solution(''), None)

if __name__ == '__main__':
    print(main())
