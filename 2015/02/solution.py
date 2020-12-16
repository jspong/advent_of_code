import sys
import unittest

class Test(unittest.TestCase):

    def tests(self):
        self.assertEquals(solution('2x3x4'), 58)
        self.assertEquals(solution('1x1x10'), 43)


def solution(s):
    parts = sorted(int(x) for x in s.split('x'))
    return 3 * parts[0] * parts[1] + 2 * parts[1] * parts[2] + 2 * parts[2] * parts[0]

if __name__ == '__main__':
    sum = 0
    for line in sys.stdin:
        sum += solution(line)
    print(sum)
