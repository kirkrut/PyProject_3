import pygame
import Blocks
import Player_comp
import random
from pygame import *
WIN_WIDTH = 600
WIN_HEIGHT = 800
PLATFORM_WIDTH = 15
PLATFORM_HEIGHT = 15
PLATFORM_COLOR = "#32CD32"
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#696969"
COLOR_COMP = "#FFFFFF"
clock = pygame.time.Clock()


def main(time1):
    pygame.init()
    run = True
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption('Labirint')
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color(BACKGROUND_COLOR))
    entities = pygame.sprite.Group()
    entities_exit = pygame.sprite.Group()
    pf_exit = []
    platforms = []
    level = [
        "----------------------------------------",
        "-  -                           -       -",
        "- --  ---------------   -  --  ------  -",
        "-     - -  -            -  -   -       -",
        "- --  - -  -   -------  -  -   -    -  -",
        "- -   - -      -        -  -   -    -  -",
        "- -   - -   ----        -  -        -  -",
        "- -   -        -  -------------------  -",
        "- -   ------   -        --             -",
        "---   -    -   ----     -    -----------",
        "- -        -      -             -   -  -",
        "- -  -     -----  - -----    -         -",
        "- -  -                  -------------  -",
        "- -  --------- -------             -   -",
        "-    -               ---------------   -",
        "- ----  --------------             -   -",
        "-    -                  - ----------   -",
        "-    --------------------        -   ---",
        "-         -   -   -     - -- -----   - -",
        "--------  -   -   -  -  - -  -       - -",
        "-      -  -   -   -  -  - -  -  ------ -",
        "-  -   -  -   -   -  -  - -  -         -",
        "-  -      -          -  - -  --------- -",
        "-  -----  ------------  ---            -",
        "-                               --------",
        "- --- ---------------------------      -",
        "- -    --     -           -            -",
        "- -     --- ---- -------  -  -  ----   -",
        "- -- --            -   -  -  -  -  -   -",
        "- -   -------      -   -  -  -  -  -   -",
        "- - -   -   ------     -  -  -  -  -   -",
        "- - -   -   -  - ----  - --  -  -  -   -",
        "- - -   -   -  -    ---      -  -  -   -",
        "- - -   -   -  -   -- ----   -  -  -   -",
        "- - -   -      -    -    --------      -",
        "- - -   -   -  -    -          -----   -",
        "- - -   -   -  -    -    ----     ---- -",
        "- - -   ------ ---  - ----  -   ---    -",
        "-           -          -               -",
        "----------------------------------------"]
    start_x = start_y = x = y = q = i = 0

    k1 = int(random.uniform(1, 38))
    while k1 == 3 or k1 == 31:
        k1 = int(random.uniform(1, 38))
    k2 = int(random.uniform(1, 38))
    while k2 == 12 or k2 == 23:
        k2 = int(random.uniform(1, 38))
    for row in level:
        for col in row:
            if col == "-" and q == k1 and i == 0:
                pf_exit = Blocks.Platform(x, y)
                entities_exit.add(pf_exit)
            elif col == "-" and q == k2 and i == 39:
                start_x = x
                start_y = y
                pf = Blocks.Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            elif col == "-":
                pf = Blocks.Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            x += PLATFORM_WIDTH
            q += 1
        y += PLATFORM_HEIGHT
        q = 0
        x = 0
        i += 1
    font = pygame.font.SysFont('arial', 30)
    hero_comp = Player_comp.Player(start_x, start_y-15, run, COLOR_COMP)
    entities.add(hero_comp)
    entities_exit.add(hero_comp)
    while run:
        time = pygame.time.get_ticks()//1000 - time1
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYDOWN and e.key == K_q):
                raise SystemExit
            if e.type == KEYDOWN and e.key == K_a:
                time1 = pygame.time.get_ticks()//1000
                main(time1)
            if e.type == KEYDOWN and e.key == K_p:
                Player_comp.Player.MOVE_SPEED= 5
            if e.type == KEYUP and e.key == K_p:
                Player_comp.Player.MOVE_SPEED = 1
        screen.blit(bg, (0, 0))
        if hero_comp.next_move == 1:
            hero_comp.move_right(platforms, pf_exit)
        elif hero_comp.next_move == 2:
            hero_comp.move_up(platforms, pf_exit)
        elif hero_comp.next_move == 3:
            hero_comp.move_left(platforms, pf_exit)
        elif hero_comp.next_move == 4:
            hero_comp.move_down(platforms, pf_exit)
        if hero_comp.run == False:
            run = False
        movements = hero_comp.movements
        entities.draw(screen)
        text_m2 = font.render(str(movements), 1, (50, 205, 50))
        text_m1 = font.render("шаги:", 1, (50, 205, 50))
        text_time1 = font.render("время:", 1, (50, 205, 50))
        text_time2 = font.render(str(time), 1, (50, 205, 50))
        text_finish = font.render("Чтобы завершить игру нажмите q", 1, (50, 205, 50))
        text_repeat = font.render("Чтобы начать игру заново нажмите a", 1, (50, 205, 50))
        place_m2 = text_m2.get_rect(center=(575, 620))
        place_m1 = text_m1.get_rect(center=(500, 620))
        place_time1 = text_time1.get_rect(center=(530, 660))
        place_time2 = text_time1.get_rect(center=(610, 660))
        place_finish = text_finish.get_rect(center=(300, 700))
        place_repeat = text_finish.get_rect(center=(300, 750))
        screen.blit(text_m1, place_m1)
        screen.blit(text_m2, place_m2)
        screen.blit(text_time1, place_time1)
        screen.blit(text_time2, place_time2)
        screen.blit(text_finish, place_finish)
        screen.blit(text_repeat, place_repeat)
        pygame.display.update()
    while True:
        clock.tick(60)
        font = pygame.font.SysFont('arial', 20)
        screen.blit(bg, (0, 0))
        text_end = font.render("Вы выйграли,нажмите а, чтобы начать сначала или q, чтобы выйти", 1, (50, 205, 50))
        place_end = text_end.get_rect(center=(300, 400))
        screen.blit(text_end, place_end)
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYDOWN and e.key == K_q):
                raise SystemExit
            if e.type == KEYDOWN and e.key == K_a:
                time1 = pygame.time.get_ticks() // 1000
                main(time1)
        pygame.display.update()


while True:
    main(0)