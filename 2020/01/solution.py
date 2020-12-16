import unittest
import sys

class Test(unittest.TestCase):

    def test_thing(self):
        pass

def main(args):
    print('test')
    nums = [int(line) for line in sys.stdin]
    for num in nums:
        for num2 in nums:
            for num3 in nums:
                if num + num2 + num3 == 2020:
                    print(num * num2 * num3)
                    return


if __name__ == '__main__':
    import os
    main(sys.argv)
