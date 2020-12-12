import os
import unittest
import sys

class Test(unittest.TestCase):

    def test_thing(self):
        pass

def is_valid(pwd):
    parts = pwd.split()
    a, b = parts[0].split('-')
    a, b = int(a), int(b)
    letter = parts[1][0]
    word = parts[2]
    try:
        is_a = int(word[a-1] == letter)
    except:
        return 0
    is_b = 0
    try:
        is_b = int(word[b-1] == letter)
    except:
        return is_a
    return is_a + is_b == 1

def main(args):
    count = sum(1 for line in sys.stdin if is_valid(line))
    print(count)


if __name__ == '__main__':
    main(sys.argv)
