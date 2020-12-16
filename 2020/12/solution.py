#!/usr/local/bin/python3
import sys

parts = []

def process_input_line(line):
    return line[0], int(line[1:])

if len(sys.argv) > 1:
    input_ = sys.argv[1]
else:
    input_ = "input.txt"

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        part = process_input_line(line)
        parts.append(part)

print(parts)

dirs = {
'N': (1,0),
'S': (-1,0),
'E': (0,1),
'W': (0,-1)
}

N = dirs['N']
S = dirs['S']
E = dirs['E']
W = dirs['W']

names = {
    N: 'N',
    E: 'E',
    W: 'W',
    S: 'S'
}

moves = {
    'R': {
        'N': E,
        'E': S,
        'S': W,
        'W': N
    },
    'L': {
        'N': W,
        'W': S,
        'S': E,
        'E': N
    }
}

def solution():
    ship = 0,0
    waypoint = 1, 10
    for action, num in parts:
        print(action, num)
        if action == 'L':
            for _ in range(num // 90):
                waypoint = waypoint[1], -waypoint[0]
                print(ship, waypoint)
        elif action == 'R':
            for _ in range(num // 90):
                waypoint = -waypoint[1], waypoint[0]
                print(ship, waypoint)
        elif action == 'F':
            ship = ship[0] + waypoint[0] * num, ship[1] + waypoint[1] * num
            print(ship, waypoint)
        else:
            new_dir = dirs[action]
            waypoint = waypoint[0] + num * new_dir[0], waypoint[1] + num * new_dir[1]
            print(ship, waypoint)
    return abs(ship[0]) + abs(ship[1])

print(solution())
