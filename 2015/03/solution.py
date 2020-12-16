import sys
import unittest

class Tests(unittest.TestCase):

    def test(self):
        self.assertEquals(solution('>'), 2)
        self.assertEquals(solution('^>v<'), 4)
        self.assertEquals(solution('^v^v^v^v^v^v'), 2)


def solution(s):
    pos = 0, 0
    steps = {
        '>': (1, 0),
        '<': (-1, 0),
        '^': (0, 1),
        'v': (0, -1)
    }
    visited = set()
    for c in s:
        visited.add(pos)
        step = steps.get(c, (0,0))
        pos = pos[0] + step[0], pos[1] + step[1]
    visited.add(pos)
    return len(visited)

if __name__ == '__main__':
    print(solution(sys.stdin.read().strip()))



