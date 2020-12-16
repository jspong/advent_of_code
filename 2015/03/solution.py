import sys
import unittest

class Tests(unittest.TestCase):

    def test(self):
        self.assertEquals(solution('^v'), 3)
        self.assertEquals(solution('^>v<'), 3)
        self.assertEquals(solution('^v^v^v^v^v'), 11)


def solution(s):
    santa = 0, 0
    robo = 0, 0
    steps = {
        '>': (1, 0),
        '<': (-1, 0),
        '^': (0, 1),
        'v': (0, -1)
    }
    visited = set()
    for i, c in enumerate(s):
        if i % 2 == 0:
            pos = santa
        else:
            pos = robo
        visited.add(pos)
        step = steps.get(c, (0,0))
        pos = pos[0] + step[0], pos[1] + step[1]
        if i % 2 == 0:
            santa = pos
        else:
            robo = pos

    visited.add(robo)
    visited.add(santa)
    return len(visited)

if __name__ == '__main__':
    print(solution(sys.stdin.read().strip()))



