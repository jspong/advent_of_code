import sys

def row(s, a, b):
    if not s:
        return a
    mid = (a + b) / 2
    if s[0] == 'B':
        return row(s[1:], mid, b)
    elif s[0] == 'F':
        return row(s[1:], a, mid)
    else:
        raise Exception(repr(s))

def col(s, a, b):
    if not s:
        return a
    mid = (a + b) / 2
    if s[0] == 'R':
        return col(s[1:], mid, b)
    elif s[0] == 'L':
        return col(s[1:], a, mid)
    else:
        raise Exception(repr(s))

def score(line):
    line = line.strip()
    return (row(line[:-3], 0, 128) * 8 + col(line[-3:], 0, 8))

result = sorted(score(line) for line in sys.stdin)

print [r for r in range(result[0], result[-1] + 1) if r not in result]
