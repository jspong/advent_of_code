import sys

board = []
for line in sys.stdin:
    board.append(list(line.strip()))

def is_stable(board, new_board):
    for line, new_line in zip(board, new_board):
        for seat, new_seat in zip(line, new_line):
            if seat != new_seat:
                return False
    return True


FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'
def is_empty(board, i, j):
    return board[i][j] in (EMPTY, FLOOR)

def adjacent(board, i, j):
    count = 0
    for pair in ((-1,1),(-1,0),(-1,-1),(0,1),(0,-1),(1,1),(1,0),(1,-1)):
        try:
            x, y = i + pair[0], j + pair[1]
            while x >= 0 and y >= 0:
                if board[x][y] == OCCUPIED:
                    count += 1
                    break
                elif board[x][y] == EMPTY:
                    break
                x += pair[0]
                y += pair[1]
        except IndexError:
            pass
    return count

while True:
    for row in board:
        print(''.join(row))
    print('')
    new_board = [[s for s in row] for row in board]
    for i in range(len(board)):
        row = board[i]
        for j in range(len(row)):
            if board[i][j] == OCCUPIED and adjacent(board, i, j) > 4:
                new_board[i][j] = EMPTY
            elif board[i][j] == EMPTY and adjacent(board, i, j) == 0:
                new_board[i][j] = OCCUPIED
            else:
                new_board[i][j] = board[i][j]
    if is_stable(board, new_board):
        break
    else:
        board = new_board

count = 0
for row in board:
    for seat in row:
        if seat == OCCUPIED:
            count+= 1
print(count)
