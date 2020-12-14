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

def gcd(x, y):
    if y > x: return gcd(y,x)
    elif y == 0:
        return x
    else:
        return gcd(y, x % y)

def are_coprime(numbers):
    print(numbers)
    numbers = [n for n in numbers if n is not None]
    print(numbers)
    for i, x in enumerate(numbers):
        for y in numbers[i+1:]:
            if gcd(x, y) != 1:
                return (x, y)
    return None

def chinese_remainder(A, M):
    return

def solution():
    assert are_coprime(schedule) is None, are_coprime(schedule)
    a, n = [i for i, x in enumerate(schedule) if x is not None], [x for x in schedule if x is not None]
    return chinese_remainder(n, a)

print(solution())
