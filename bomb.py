import time


class Bomb:
    def __init__(self, man, board_grid):
        self.state = 3
        self.time = time.time()
        self.timeout = 0.8
        self.explosion_timeout = 0.6
        self.posx = man.posx
        self.posy = man.posy
        self.e = False
        self.r = [1, 0]
        man.p = 8
        board_grid[self.posx][self.posy] = 8

    def change(self, board_grid, man, enemy_list):
        self.r = [1, 0]
        if time.time() - self.time > self.timeout and not self.e:
            self.time = time.time()
            self.state -= 1
            board_grid[self.posx][self.posy] -= 1
            if man.posx == self.posx and man.posy == self.posy:
                man.p = board_grid[self.posx][self.posy]
        if self.state < 1:
            board_grid[self.posx][self.posy] = 0
            if self.e:
                self.explosion(board_grid, man, enemy_list)
                return self.r
            else:
                self.e = True
                self.time = time.time()
                self.explosion(board_grid, man, enemy_list)
                return self.r
        return self.r

    def explosion(self, board_grid, man, enemy_list):
        if time.time() - self.time > self.explosion_timeout:
            if self.posx > 0 and board_grid[self.posx - 1][self.posy] != 2:
                if board_grid[self.posx - 1][self.posy] == 1:
                    self.r[1] += 20
                board_grid[self.posx - 1][self.posy] = 0
            if self.posx < 16 and board_grid[self.posx + 1][self.posy] != 2:
                if board_grid[self.posx + 1][self.posy] == 1:
                    self.r[1] += 20
                board_grid[self.posx + 1][self.posy] = 0
            if self.posy > 0 and board_grid[self.posx][self.posy - 1] != 2:
                if board_grid[self.posx][self.posy - 1] == 1:
                    self.r[1] += 20
                board_grid[self.posx][self.posy - 1] = 0
            if self.posy < 18 and board_grid[self.posx][self.posy + 1] != 2:
                if board_grid[self.posx][self.posy + 1] == 1:
                    self.r[1] += 20
                board_grid[self.posx][self.posy + 1] = 0
            self.r[0] = 0
            return self.r
        else:
            board_grid[self.posx][self.posy] = 9
            if self.posx > 0 and board_grid[self.posx - 1][self.posy] != 2:
                if board_grid[self.posx - 1][self.posy] == 1:
                    self.r[1] += 20
                board_grid[self.posx - 1][self.posy] = 9
            if self.posx < 16 and board_grid[self.posx + 1][self.posy] != 2:
                if board_grid[self.posx + 1][self.posy] == 1:
                    self.r[1] += 20
                board_grid[self.posx + 1][self.posy] = 9
            if self.posy > 0 and board_grid[self.posx][self.posy - 1] != 2:
                if board_grid[self.posx][self.posy - 1] == 1:
                    self.r[1] += 20
                board_grid[self.posx][self.posy - 1] = 9
            if self.posy < 18 and board_grid[self.posx][self.posy + 1] != 2:
                if board_grid[self.posx][self.posy + 1] == 1:
                    self.r[1] += 20
                board_grid[self.posx][self.posy + 1] = 9
            for e in enemy_list:
                if e.posx == self.posx:
                    if abs(self.posy - e.posy) < 2:
                        enemy_list.remove(e)
                elif e.posy == self.posy:
                    if abs(self.posx - e.posx) < 2:
                        enemy_list.remove(e)
            if man.posx == self.posx:
                if abs(self.posy - man.posy) < 2:
                    man.dead = 1
            elif man.posy == self.posy:
                if abs(self.posx - man.posx) < 2:
                    man.dead = 1
            self.r[0] = 1
            return self.r
