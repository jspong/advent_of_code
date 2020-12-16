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
    return sum(1 if c == '(' else -1 for c in s)

if __name__ == '__main__':
    print(solution(sys.stdin.readline().strip()))
