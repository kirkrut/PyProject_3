from pygame import*
PLATFORM_WIDTH = 15
PLATFORM_HEIGHT = 15
PLATFORM_COLOR = "#32CD32"


class Platform(sprite.Sprite):
    def __init__(self,  x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
