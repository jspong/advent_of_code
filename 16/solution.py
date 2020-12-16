#!/usr/local/bin/python3
import collections
import copy
import itertools
import sys

if len(sys.argv) > 1:
    input_ = sys.argv[1]
else:
    input_ = "input.txt"

my_ticket = None

def validate(rules, ticket):
    tse = 0
    for part in ticket:
        part = int(part)
        for name, rule in rules.items():
            if any(part in r for r in rule):
                break
        else:
            tse += 1
    return tse

with open(sys.argv[1]) as f:
    rules = collections.defaultdict(list)
    section = 'rules'
    tickets = []
    for line in f:
        line = line.strip()
        if section == 'rules':
            if not line:
                section = 'your tickets'
                continue
            name, rule = line.split(':')
            for part in rule.split(' or '):
                start, end = part.strip().split('-')
                start, end = int(start), int(end)
                rules[name].append(list(range(start, end+1)))
        elif section == 'your tickets':
            if ',' in line:
                my_ticket = [int(x) for x in line.split(',')]
            if line.strip() == 'nearby tickets:':
                section = 'other'
                continue
        elif section == 'other':
            if not validate(rules, line.split(',')):
                tickets.append([int(x) for x in line.split(',')])

def is_valid(rule, index):
    return all(any(ticket[index] in r for r in rule) for ticket in tickets)

possibilities = { name: [is_valid(rule, i) for i in range(len(tickets[0]))]
                  for name, rule in rules.items() }

def search(i):
    if i == len(tickets[0]):
        return []
    if not any(any(p) for p in possibilities.values()):
        return None
    rules = sorted(possibilities.items(), key=lambda x: (True in x[1], -sum(p for p in x[1])), reverse=True)
    for name, rule in rules:
        for i, valid in enumerate(rule):
            if not valid:
                continue
            old_values = update(name, i)
            step = search(i+1)
            if step is None:
                revert(old_values, i)
                del choices[name]
                return None
            else:
                return step + [(name, i)]
    return None

def update(name, index):
    old = {}
    for rule, possible in possibilities.items():
        old[rule] = list(possible)
        if rule == name:
            for i in range(len(possible)):
                possible[i] = False
        else:
            possible[index] = False
    return old

def revert(old_values, index):
    for rule, value in old_values.items():
        possibilities[rule] = value

solution = dict(search(0))
print(my_ticket)
print(solution)

product = 1
for name, position in solution.items():
    if name.startswith('departure'):
        product *= my_ticket[position]
print(product)
