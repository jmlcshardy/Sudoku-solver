import pygame
from time import sleep

pygame.init()
screen = pygame.display.set_mode((900, 633))

pygame.display.set_caption("Sudoku")

tile_size = 630/9

font = pygame.font.SysFont('arial', 30)

registering = False

speed = 1

sudoku_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]


class Button:
    def __init__(self, x, y, text, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text
        self.color = (0, 0, 0)

    def draw(self, color):
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height), 0, 3)
        text = font.render(self.text, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text, text_rect)

    def detect_collide(self, x, y):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        else:
            return False


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


def find_next_zero(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def gui():

    pygame.event.pump()

    screen.fill((255, 255, 255))

    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(screen, (0, 0, 0), (1, i * tile_size + 1), (631, i * tile_size + 1), 3)
        else:
            pygame.draw.line(screen, (100, 100, 100), (1, i * tile_size + 1), (631, i * tile_size + 1))

    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(screen, (0, 0, 0), (i * tile_size + 1, 1), (i * tile_size + 1, 631), 3)
        else:
            pygame.draw.line(screen, (100, 100, 100), (i * tile_size + 1, 1), (i * tile_size + 1, 631))

    for i in range(9):
        for j in range(9):
            if sudoku_board[i][j] != 0:
                x = j * tile_size + tile_size/3 + 5
                y = i * tile_size + tile_size/3 - 5
                num = font.render(str(sudoku_board[i][j]), True, (0, 0, 0))
                screen.blit(num, (x, y))


def show_buttons():
    global speed, registering

    mouse_square = [(mousePos[0] // tile_size) * tile_size, (mousePos[1] // tile_size) * tile_size]

    if 0 < mousePos[0] < 630 and 0 < mousePos[1] < 630:
        inBoard = True
    else:
        inBoard = False

    if mouse[0] and inBoard:
        registering = [mouse_square[1]//tile_size, mouse_square[0]//tile_size]

    if registering and inBoard:

        pygame.draw.rect(screen, (0, 0, 255), (registering[1] * tile_size + 1, registering[0] * tile_size + 1, tile_size
                                               , tile_size), 3)

        pre_reg = sudoku_board[int(registering[0])][int(registering[1])]

        # There is definitely a better way
        if keys[pygame.K_0]:
            sudoku_board[int(registering[0])][int(registering[1])] = 0
        if keys[pygame.K_1]:
            sudoku_board[int(registering[0])][int(registering[1])] = 1
        if keys[pygame.K_2]:
            sudoku_board[int(registering[0])][int(registering[1])] = 2
        if keys[pygame.K_3]:
            sudoku_board[int(registering[0])][int(registering[1])] = 3
        if keys[pygame.K_4]:
            sudoku_board[int(registering[0])][int(registering[1])] = 4
        if keys[pygame.K_5]:
            sudoku_board[int(registering[0])][int(registering[1])] = 5
        if keys[pygame.K_6]:
            sudoku_board[int(registering[0])][int(registering[1])] = 6
        if keys[pygame.K_7]:
            sudoku_board[int(registering[0])][int(registering[1])] = 7
        if keys[pygame.K_8]:
            sudoku_board[int(registering[0])][int(registering[1])] = 8
        if keys[pygame.K_9]:
            sudoku_board[int(registering[0])][int(registering[1])] = 9

        if keys[pygame.K_ESCAPE] or pre_reg != sudoku_board[int(registering[0])][int(registering[1])]:
            registering = False

    if keys[pygame.K_s]:
        main()

    showSpeed = font.render("Speed", True, (0, 0, 0))
    screen.blit(showSpeed, (730, 500))

    speed1 = Button(670, 550, ">", 50, 50)
    if speed1.detect_collide(mousePos[0], mousePos[1]):
        speed1.draw((3, 37, 126))
        if mouse[0]:
            speed = 1
    elif speed == 1:
        speed1.draw((3, 37, 126))
    else:
        speed1.draw((0, 191, 255))

    speed2 = Button(740, 550, ">>", 50, 50)
    if speed2.detect_collide(mousePos[0], mousePos[1]):
        speed2.draw((3, 37, 126))
        if mouse[0]:
            speed = 2
    elif speed == 2:
        speed2.draw((3, 37, 126))
    else:
        speed2.draw((0, 191, 255))

    speed3 = Button(810, 550, ">>>", 50, 50)
    if speed3.detect_collide(mousePos[0], mousePos[1]):
        speed3.draw((3, 37, 126))
        if mouse[0]:
            speed = 3
    elif speed == 3:
        speed3.draw((3, 37, 126))
    else:
        speed3.draw((0, 191, 255))

    solve = Button(693, 280, "Solve", 150, 70)
    if solve.detect_collide(mousePos[0], mousePos[1]):
        solve.draw((3, 37, 126))
        if mouse[0]:
            main()
    else:
        solve.draw((0, 191, 255))

    reset = Button(723, 180, "Reset", 90, 70)
    if reset.detect_collide(mousePos[0], mousePos[1]):
        reset.draw((200, 0, 40))
        if mouse[0]:
            for i in range(9):
                for j in range(9):
                    sudoku_board[i][j] = 0
    else:
        reset.draw((255, 51, 51))
    pygame.display.update()


def main():
    found = []
    next_zero = find_next_zero(sudoku_board)
    if next_zero is None:
        return
    else:
        col, row = next_zero
    currentNum = 1
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
                sudoku_board[col][row] = 0
            else:
                raise Exception("Board can't be solved")
        if speed < 3:
            gui()
            pygame.display.update()
        if speed < 2:
            sleep(.05)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    mousePos = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pressed()

    gui()
    show_buttons()

    pygame.display.update()

pygame.quit()