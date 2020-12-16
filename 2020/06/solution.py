def groups(stream):
    group = []
    for line in stream:
        if line.strip():
            group.append(line.strip())
        else:
            yield group
            group = []
    yield group

def matches(group):
    count = 0
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if all(letter in x for x in group):
            count += 1
    return count

import sys
print sum(matches(g) for g in groups(sys.stdin))
