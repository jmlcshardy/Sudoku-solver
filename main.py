sudoku_board = [[9, 0, 0, 0, 0, 0, 1, 0, 6],
                [6, 4, 0, 0, 0, 0, 0, 0, 0],
                [0, 2, 7, 0, 0, 5, 0, 0, 3],
                [3, 0, 4, 0, 0, 9, 5, 0, 1],
                [0, 0, 5, 0, 0, 0, 4, 2, 0],
                [0, 6, 0, 5, 0, 4, 0, 0, 8],
                [0, 9, 0, 7, 5, 0, 0, 3, 0],
                [0, 0, 8, 6, 0, 0, 7, 4, 0],
                [0, 0, 0, 0, 0, 0, 0, 9, 0]]


def check_square(pos1, pos2, board):
    numbers = [num for num in range(1, 10)]
    for i in range(9):
        if board[pos2][i] in numbers:
            numbers.remove(board[pos2][i])
        if board[i][pos1] in numbers:
            numbers.remove(board[i][pos1])
    row_start = (pos2 // 3) * 3
    col_start = (pos1 // 3) * 3
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if board[i][j] in numbers:
                numbers.remove(board[i][j])

    if len(numbers) == 1:
        return numbers[0]
    else:
        return 0


def check_zeros(board):
    for i in board:
        for j in i:
            if j == 0:
                return False
    return True


zeros = check_zeros(sudoku_board)

times = 0
while not zeros:
    for i in range(9):
        for j in range(9):
            if sudoku_board[i][j] == 0:
                replace_num = check_square(i, j, sudoku_board)
                sudoku_board[i][j] = replace_num
                if replace_num != 0:
                    print(sudoku_board)
    zeros = check_zeros(sudoku_board)
    times += 1

    print(times)
print(sudoku_board)