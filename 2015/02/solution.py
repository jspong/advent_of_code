import sys
import unittest

class Test(unittest.TestCase):

    def tests(self):
        self.assertEquals(solution('2x3x4'), 34)
        self.assertEquals(solution('1x1x10'), 14)


def solution(s):
    a, b, c = sorted(int(x) for x in s.split('x'))
    perimeter = 2 * a + 2 * b
    return perimeter + a * b * c

if __name__ == '__main__':
    sum = 0
    for line in sys.stdin:
        sum += solution(line)
    print(sum)
