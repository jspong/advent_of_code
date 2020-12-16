#!/usr/local/bin/python3
import collections
import copy
import itertools
import sys

parts = []



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
    tse = 0
    tickets = []
    for line in f:
        line = line.strip()
        if section == 'rules':
            if not line.strip():
                section = 'your tickets'
                continue
            name, rule = line.strip().split(':')
            for part in rule.split(' or '):
                start, end = part.strip().split('-')
                start, end = int(start), int(end)
                rules[name].append(list(range(start, end+1)))
        elif section == 'your tickets':
            if ',' in line:
                my_ticket = [int(x) for x in line.strip().split(',')]
            if line.strip() == 'nearby tickets:':
                section = 'other'
                continue
        elif section == 'other':
            if not validate(rules, line.strip().split(',')):
                tickets.append([int(x) for x in line.strip().split(',')])

spots = {}
options = {}

def is_in_rule(value, rule):
    return any(value in r for r in rule)

def rule_match(ticket, rule, index):
    return is_in_rule(ticket[index], rule)

def is_valid(rule, index):
    return all(rule_match(ticket, rule, index) for ticket in tickets)

possibilities = { name: [is_valid(rule, i) for i in range(len(tickets[0]))]
                  for name, rule in rules.items() }

ticket = tickets[0]
choices = {}
def search(i):
    done = False
    for name, rule in possibilities.items():
        if name in choices:
            break
        for part in rule:
            if part:
                break
        else:
            done = True
            break
    if i == len(ticket):
        return []
    if done:
        return None
    rules = sorted(possibilities.items(), key=lambda x: (True in x[1], -sum(p == True for p in x[1])), reverse=True)
    for name, rule in rules:
        for i, valid in enumerate(rule):
            if not valid:
                continue
            old_values = update(name, i)
            choices[name] = i
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
                possible[i] = None
        else:
            possible[index] = None
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
