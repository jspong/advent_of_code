import sys

def get_board():
    lines = []
    for line in sys.stdin:
        lines.append([c == '#' for c in line if c in ('#', '.')])
    print('\n'.join(''.join(str(int(i)) for i in line) for line in lines ))
    return lines

def run_test(board, slope_x, slope_y):
    x, y = 0, 0
    count = 0
    width = len(board[0])
    while y < len(board):
        for i in range(width):
            if i == x:
                print 'X' if board[y][x] else 'O',
            else:
                print '#' if board[y][i] else '.',
        print
        count += board[y][x]
        x = (x + slope_x) % width
        y += slope_y
    return count

if __name__ == '__main__':
    board = get_board()
    solutions = [
        run_test(board, 1,1),
        run_test(board, 3,1),
        run_test(board, 5,1),
        run_test(board, 7,1),
        run_test(board, 1,2)
    ]
    product = 1
    for solution in solutions:
        product *= solution
    print product
