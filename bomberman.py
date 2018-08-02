from __future__ import print_function
import sys
import time
import random
from getchunix import *
from datetime import datetime
from timeout import *
from levels import *
import person
import board
import bomb

random.seed(datetime.now())

score = 0
levels = list()
levels.append(Level(0.2, 0.6, 0.6, 3))
levels.append(Level(0.1, 0.3, 0.3, 5))
levels.append(Level(0.1, 0.1, 0.1, 7))


def level_fun(level):
    global score
    board_grid = [[0 for j in range(19)] for i in range(17)]
    b = board.Board(17, 19, board_grid)
    os.system('clear')
    b.print_message("LEVEL " + str(levels.index(level) + 1))
    time.sleep(2)
    man = person.Bomberman(board_grid)
    bomb_list = []
    enemies = []
    for _ in range(level.enemy_no):
        enemies.append(person.Enemy(board_grid))

    pgetch = [time.time(), '0']

    def update():
        global score
        if bomb_list.__len__() != 0:
            r = bomb_list[0].change(board_grid, man, enemies)
            if r[0] == 0:
                bomb_list.pop()
            score += r[1]
        for e in enemies:
            e.move(board_grid, man, level.enemy_time)
        os.system('clear')
        b.print_board(board_grid)
        if enemies.__len__() == 0:
            score += (level.enemy_no - enemies.__len__()) * 100
            return 1
        return 0

    while man.dead is 0:

        @timeout(level.timeout)
        def loop(p):
            global score
            c = getch()
            getchtime = time.time()
            if getchtime - p[0] < level.man_time and c in ['w', 's', 'a', 'd']:
                return p
            if c == 'q':
                score += (level.enemy_no - enemies.__len__()) * 100
                msg = "Your score is " + str(score)
                os.system('clear')
                b.print_message(msg)
                sys.exit(0)
            if c in ['w', 's', 'a', 'd', 'x', 'b', 'o']:
                if c == 'w':
                    man.move_up(board_grid, man)
                elif c == 's':
                    man.move_down(board_grid, man)
                elif c == 'a':
                    man.move_left(board_grid, man)
                elif c == 'd':
                    man.move_right(board_grid, man)
                elif c in ['x', 'b', 'o']:
                    if bomb_list.__len__() == 0:
                        bomb_list.append(bomb.Bomb(man, board_grid))
                u = update()
                if u == 1:
                    return TimeoutError
            p[0] = getchtime
            p[1] = c
            return p

        try:
            pgetch = loop(pgetch)
        except TimeoutError:
            u = update()
            if u == 1:
                return
    update()
    score += (level.enemy_no - enemies.__len__()) * 100
    os.system('clear')
    msg = "YOU DIED. Your score is " + str(score)
    b.print_message(msg)
    sys.exit(0)


for level in levels:
    level_fun(level)

board_grid = [[0 for j in range(19)] for i in range(17)]
b = board.Board(17, 19, board_grid)
msg = "YOU WON. Your score is " + str(score)
b.print_message(msg)
sys.exit(0)
