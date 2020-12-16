import itertools
import operator
import sys

PREAMBLE = 25

window = []

def is_sum(num, window):
    return any(num == a + b for a, b in itertools.permutations(window, 2))

def find_range(num, window):
    print(num, window)
    def all_ranges():
        for i in range(len(window)):
            for j in range(i, len(window)):
                sub_window = window[i:j]
                x = sum(sub_window)
                if x == num:
                    print(sub_window)
                    yield sub_window
                    break
                elif x > num:
                    break

    return next(all_ranges())



results = []
all_nums = []
for line in sys.stdin:
    num = int(line)
    all_nums.append(num)
    if len(window) < PREAMBLE:
        print(num)
        window.append(num)
        continue
    if is_sum(num, window):
        print(num, 'VALID')
        results.append((num, 'VALID'))
    else:
        print(num, 'INVALID')
        results.append((num, 'INVALID'))
        cont = find_range(num, all_nums)
        print(min(cont) + max(cont))
        break
    window.append(num)
    window[:1] = []


