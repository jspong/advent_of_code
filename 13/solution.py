#!/usr/local/bin/python3
import sys
import operator

parts = []

def process_input_line(line):
    return [None if x == 'x' else int(x) for x in line.split(',')]

if len(sys.argv) > 1:
    input_ = sys.argv[1]
else:
    input_ = "input.txt"

with open(sys.argv[1]) as f:
    _ = int(f.readline())
    schedule = process_input_line(f.readline())

def inverse(a, b):
    def _inverse(a, b):
        if a == 0:
            return b, 0, 1

        g, x1, y1 = _inverse(b % a, a)
        x = y1 - (b // a) * x1
        y = x1

        return g, x, y
    _, x, _ = _inverse(a, b)
    return x % b

def product(n):
    value = 1
    for x in n:
        value *= x
    return value

def chinese_remainder(A, M):
    x = 0
    prod = product(M)
    for a, m in zip(A, M):
        b = prod // m
        x += a * b * inverse(b, m)
    x %= prod
    return x

def solution():
    a, m = [-i for i, x in enumerate(schedule) if x is not None], [x for x in schedule if x is not None]
    answer = chinese_remainder(a, m)
    for a, m in zip(a, m):
        print(answer % m == a)
    return answer

print(solution())
