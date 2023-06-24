sudoku_board = []

for i in range(9):
    row = input(f"Enter row {i + 1}: ")
    sudoku_board.append([int(char) for char in row])


def check_square(pos1, pos2, board, number):
    for i in range(9):
        if board[i][pos2] == number or board[pos1][i] == number:
            return False
    row_start = (pos1 // 3) * 3
    col_start = (pos2 // 3) * 3
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if board[i][j] == number:
                return False

    return True


# https://stackoverflow.com/questions/72159405/how-to-print-sudoku-board-using-python-class
def print_board(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - - - ")
        for col in range(len(board[0])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")

            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")


def find_next_zero(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


print_board(sudoku_board)

found = []
col, row = find_next_zero(sudoku_board)
currentNum = 1
numFound = True
solved = False

while not solved:
    numFound = False
    while not numFound and currentNum < 10:
        if check_square(col, row, sudoku_board, currentNum):
            sudoku_board[col][row] = currentNum
            numFound = True
            found.append([col, row, currentNum])
            currentNum = 1
            next_zero = find_next_zero(sudoku_board)
            if next_zero is None:
                solved = True
            else:
                col, row = next_zero

        else:
            currentNum += 1

    if not numFound:
        if found:
            col, row, currentNum = found.pop()
            currentNum += 1
            print(found)
            sudoku_board[col][row] = 0
        else:
            print_board(sudoku_board)
            raise Exception("Board can't be solved")

print_board(sudoku_board)
