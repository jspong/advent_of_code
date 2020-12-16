import sys
import unittest

class Tests(unittest.TestCase):
    def test_floor0(self):
        self.assertEquals(solution('()()'), 0)
        self.assertEquals(solution('(())'), 0)

    def test_floor3(self):
        self.assertEquals(solution('((('), 3)
        self.assertEquals(solution('(()(()('), 3)
        self.assertEquals(solution('))((((('), 3)

    def test_basement(self):
        self.assertEquals(solution('())'), -1)
        self.assertEquals(solution('))('), -1)

    def test_floor_minus3(self):
        self.assertEquals(solution(')))'), -3)
        self.assertEquals(solution(')())())'), -3)

def solution(s):
    floor = 0
    for i, c in enumerate(s, start=1):
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        if floor == -1:
            return i

if __name__ == '__main__':
    print(solution(sys.stdin.readline().strip()))
