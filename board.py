from __future__ import print_function
import random
from random import randint
from datetime import datetime

random.seed(datetime.now())
CSI = "\x1B["
reset = CSI+"m"


def print_wall():
    print(CSI + "1;37;47m" + ' ' + reset, end='')


def print_space():
    print(CSI + "1;37;40m" + ' ' + reset, end='')


def print_brick():
    print(CSI + "0;30;42m" + '#' + reset, end='')


class Board:
    x = 17
    y = 19

    def __init__(self, x, y, board_grid):

        self.x = x
        self.y = y

        for i in range(1, self.x, 2):
            for j in range(1, self.y, 2):
                board_grid[i][j] = 2

        for _ in range(20):
            i = randint(0, 8)
            j = randint(0, 9)
            board_grid[i*2][j*2] = 1
            i = randint(0, 7)
            j = randint(0, 8)
            board_grid[i * 2 + 1][j * 2] = 1
            i = randint(0, 7)
            j = randint(0, 8)
            board_grid[i * 2][j * 2 + 1] = 1

        board_grid[0][0] = board_grid[0][1] = board_grid[1][0] = 0

    def print_board(self, board_grid):

        for i in range(2):
            for j in range(4*self.y+8):
                print_wall()
            print(end='\n')

        for i in range(2*self.x):
            print_wall()
            print_wall()
            print_wall()
            print_wall()
            for j in range(4*self.y):
                if board_grid[i//2][j//4] == 2:
                    print_wall()
                elif board_grid[i//2][j//4] == 1:
                    print_brick()
                elif board_grid[i//2][j//4] == 4:
                    if i % 2 == 0:
                        if j % 4 == 0:
                            print(CSI + "0;37;44m" + '[' + reset, end='')
                        elif j % 4 == 1 or j % 4 == 2:
                            print(CSI + "0;37;44m" + 'o' + reset, end='')
                        else:
                            print(CSI + "0;37;44m" + ']' + reset, end='')
                    else:
                        if j % 4 == 0:
                            print_space()
                            # print(CSI + "0;37;44m" + '\\' + reset, end='')
                        elif j % 4 == 3:
                            # print(CSI + "0;37;44m" + '/' + reset, end='')
                            print_space()
                        elif j % 4 == 1:
                            print(CSI + "0;37;44m" + ']' + reset, end='')
                        else:
                            print(CSI + "0;37;44m" + '[' + reset, end='')
                elif board_grid[i//2][j//4] == 5:
                    if i % 2 == 1:
                        if j % 4 == 0:
                            print(CSI + "0;37;41m" + '(' + reset, end='')
                        elif j % 4 == 1 or j % 4 == 2:
                            print(CSI + "0;37;41m" + 'o' + reset, end='')
                        else:
                            print(CSI + "0;37;41m" + ')' + reset, end='')
                    else:
                        if j % 4 == 0 or j % 4 == 3:
                            print_space()
                        elif j % 4 == 1:
                            print(CSI + "0;37;41m" + '!' + reset, end='')
                        else:
                            print(CSI + "0;37;41m" + '!' + reset, end='')
                elif board_grid[i//2][j//4] in [6, 7, 8]:
                    if j % 4 == 0:
                        print(CSI + "2;35;43m" + '[' + reset, end='')
                    elif j % 4 == 1 or j % 4 == 2:
                        m = str(board_grid[i//2][j//4]-5)
                        print(CSI + "2;35;43m" + m + reset, end='')
                    else:
                        print(CSI + "2;35;43m" + ']' + reset, end='')
                elif board_grid[i//2][j//4] == 9:
                    print(CSI + "2;35;43m" + 'o' + reset, end='')
                else:
                    print_space()
            print_wall()
            print_wall()
            print_wall()
            print_wall()
            print(end='\n')

        for i in range(2):
            for j in range(4*self.y+8):
                print_wall()
            print(end='\n')

    def print_message(self, message):
        ln = len(message)

        for i in range(2):
            for j in range(4*self.y+8):
                print_wall()
            print(end='\n')

        for i in range(2*self.x):
            print_wall()
            print_wall()
            print_wall()
            print_wall()
            if i == self.x:
                for j in range(2 * self.y - (ln + 1) // 2):
                    print_space()
                print(CSI + "0;37;40m" + message + reset, end='')
                for j in range(2 * self.y - ln + (ln + 1) // 2):
                    print_space()
            else:
                for j in range(4 * self.y):
                    print_space()
            print_wall()
            print_wall()
            print_wall()
            print_wall()
            print(end='\n')

        for i in range(2):
            for j in range(4*self.y+8):
                print_wall()
            print(end='\n')
