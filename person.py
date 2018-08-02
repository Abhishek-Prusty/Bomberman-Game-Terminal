import random
import time
from datetime import datetime
from random import randint

random.seed(datetime.now())


class Person:
    posx = posy = value = p = 0

    def move_up(self, board_grid, b):
        if self.posx <= 0:
            return 0
        elif self.value == 4 and board_grid[self.posx - 1][self.posy] == 5:
            self.dead = 1
        elif self.value == 5 and board_grid[self.posx - 1][self.posy] == 4:
            b.dead = 1
            board_grid[self.posx][self.posy] = self.p
            self.posx -= 1
            board_grid[self.posx][self.posy] = self.value
            self.p = 0
            return 1
        elif board_grid[self.posx - 1][self.posy] != 0:
            return 0
        else:
            board_grid[self.posx][self.posy] = self.p
            self.posx -= 1
            board_grid[self.posx][self.posy] = self.value
            self.p = 0
            return 1

    def move_down(self, board_grid, b):
        if self.posx > 15:
            return 0
        elif self.value == 4 and board_grid[self.posx + 1][self.posy] == 5:
            self.dead = 1
        elif self.value == 5 and board_grid[self.posx + 1][self.posy] == 4:
            b.dead = 1
            board_grid[self.posx][self.posy] = self.p
            self.posx += 1
            board_grid[self.posx][self.posy] = self.value
            self.p = 0
            return 1
        elif board_grid[self.posx + 1][self.posy] != 0:
            return 0
        else:
            board_grid[self.posx][self.posy] = self.p
            self.posx += 1
            board_grid[self.posx][self.posy] = self.value
            self.p = 0
            return 1

    def move_left(self, board_grid, b):
        if self.posy <= 0:
            return 0
        elif self.value == 4 and board_grid[self.posx][self.posy - 1] == 5:
            self.dead = 1
        elif self.value == 5 and board_grid[self.posx][self.posy - 1] == 4:
            b.dead = 1
            board_grid[self.posx][self.posy] = self.p
            self.posy -= 1
            board_grid[self.posx][self.posy] = self.value
            self.p = 0
            return 1
        elif board_grid[self.posx][self.posy - 1] != 0:
            return 0
        else:
            board_grid[self.posx][self.posy] = self.p
            self.posy -= 1
            board_grid[self.posx][self.posy] = self.value
            self.p = 0
            return 1

    def move_right(self, board_grid, b):
        if self.posy > 17:
            return 0
        elif self.value == 4 and board_grid[self.posx][self.posy + 1] == 5:
            self.dead = 1
        elif self.value == 5 and board_grid[self.posx][self.posy + 1] == 4:
            b.dead = 1
            board_grid[self.posx][self.posy] = self.p
            self.posy += 1
            board_grid[self.posx][self.posy] = self.value
            self.p = 0
            return 1
        elif board_grid[self.posx][self.posy + 1] != 0:
            return 0
        else:
            board_grid[self.posx][self.posy] = self.p
            self.posy += 1
            board_grid[self.posx][self.posy] = self.value
            self.p = 0
            return 1


class Bomberman(Person):
    value = 4

    def __init__(self, board_grid):
        self.posx = 0
        self.posy = 0
        self.dead = 0
        board_grid[self.posx][self.posy] = self.value

    def is_dead(self, board_grid):
        if board_grid[self.posx][self.posy] == 5:
            self.dead = 1


class Enemy(Person):
    value = 5

    def __init__(self, board_grid):
        x = randint(0, 2)
        if x == 0:
            i = randint(2, 8)
            j = randint(2, 9)
            self.posx = i * 2
            self.posy = j * 2
        elif x == 1:
            i = randint(2, 7)
            j = randint(2, 8)
            self.posx = i * 2 + 1
            self.posy = j * 2
        else:
            i = randint(2, 7)
            j = randint(2, 8)
            self.posx = i * 2
            self.posy = j * 2 + 1
        board_grid[self.posx][self.posy] = self.value
        self.prtime = time.time()
        self.moves = [self.move_left, self.move_up]
        self.moves.append(self.move_right)
        self.moves.append(self.move_down)

    def move(self, board_grid, b, enemy_time):
        if time.time() - self.prtime < enemy_time:
            return 0
        x = randint(0, 3)
        for i in range(4):
            if self.moves[(x + i) % 4](board_grid, b) == 1:
                break
        self.prtime = time.time()
        return 1
