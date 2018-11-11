from pygame import *

MOVE_SPEED = 1
WIDTH = 15
HEIGHT = 15
movements = 1


class Player(sprite.Sprite):
    def __init__(self, x, y, run, COLOR):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.startX = x
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.run = run
        self.movements = movements
        self.xvector = 0
        self.yvector = -1
        self.next_move = 1

    def move_right(self, platforms, pf_exit):
        self.xvector = 0
        self.yvector = 0
        self.xvel = MOVE_SPEED
        self.yvel = MOVE_SPEED
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
        self.collide_exit(pf_exit)
        if self.yvector != -1:
            self.movements += 1
            self.next_move = 4
        elif self.xvector == 0:
            self.next_move = 1
        elif self.xvector == 1:
            self.movements += 1
            self.next_move = 2

    def move_up(self, platforms, pf_exit):
        self.xvector = 0
        self.yvector = 0
        self.xvel = MOVE_SPEED
        self.yvel = -MOVE_SPEED
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
        self.collide_exit(pf_exit)
        if self.xvector != 1:
            self.movements += 1
            self.next_move = 1
        elif self.yvector == 0:
            self.next_move = 2
        elif self.yvector == 1:
            self.movements += 1
            self.next_move = 3

    def move_left(self, platforms, pf_exit):
        self.xvector = 0
        self.yvector = 0
        self.xvel = -MOVE_SPEED
        self.yvel = -MOVE_SPEED
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
        self.collide_exit(pf_exit)
        if self.yvector == 0:
            self.movements += 1
            self.next_move = 2
        elif self.xvector != -1:
            self.next_move = 3
        elif self.xvector == -1:
            self.movements += 1
            self.next_move = 4

    def move_down(self, platforms, pf_exit):
        self.xvector = 0
        self.yvector = 0
        self.yvel = MOVE_SPEED
        self.xvel = -MOVE_SPEED
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
        self.collide_exit(pf_exit)
        if self.xvector == 0:
            self.movements += 1
            self.next_move = 3
        elif self.yvector != -1:
            self.next_move = 4
        elif self.yvector == -1:
            self.movements += 1
            self.next_move = 1

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.x -= 1*MOVE_SPEED
                    self.xvector = 1
                if xvel < 0:
                    self.rect.x += 1*MOVE_SPEED
                    self.xvector = -1
                if yvel > 0:
                    self.rect.y -= 1*MOVE_SPEED
                    self.yvector = -1
                if yvel < 0:
                    self.rect.y += 1*MOVE_SPEED
                    self.yvector = 1

    def collide_exit(self, pf_exit):
        if sprite.collide_rect(self, pf_exit):
            self.run = False
