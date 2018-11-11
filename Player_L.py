from pygame import *

MOVE_SPEED = 5
WIDTH = 15
HEIGHT = 15


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

    def update(self, left, right, up, down, platforms, pf_exit):
        if up:
            self.yvel= -MOVE_SPEED
        if left:
            self.xvel = -MOVE_SPEED
        if right:
            self.xvel = MOVE_SPEED
        if not (left or right):
            self.xvel = 0
        if down:
            self.yvel= MOVE_SPEED
        if not (up or down):
            self.yvel = 0
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
        self.collide_exit(pf_exit)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if xvel > 0:
#                    self.rect.right = p.rect.left
                    self.rect.x -= MOVE_SPEED
                if xvel < 0:
                    self.rect.x += MOVE_SPEED
#                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.y -= MOVE_SPEED
#                    self.rect.bottom = p.rect.top
                if yvel < 0:
                    self.rect.y += MOVE_SPEED
#                    self.rect.top = p.rect.bottom

    def collide_exit(self, pf_exit):
        if sprite.collide_rect(self, pf_exit):
            self.run = False
