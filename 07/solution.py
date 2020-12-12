import collections
import networkx
import re
import sys

rules = collections.defaultdict(dict)

for line in sys.stdin:
    line = line.strip()
    container, _, contents = line.partition(' contain ')
    container = container[:-5]
    contents = contents[:-1].split(', ')
    for content in contents:
        if content.endswith('bag'):
            content = content[:-3]
        elif content.endswith('bags'):
            content = content[:-4]
        n, type_ = content.strip().split(' ', 1)
        if n == 'no':
            continue
        rules[container][type_] = int(n)

def search(type_):
    count = 1
    for contents in rules[type_]:
        print("`{}` `{}` `{}`".format(type_, contents, rules[type_][contents]))
        count += rules[type_][contents] * search(contents)
    return count

print(search('shiny gold') - 1)
