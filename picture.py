import pygame as pg
from pygame.draw import *
from random import *

pg.init()
a = 600
b = 850
FPS = 30
screen = pg.display.set_mode((a, b))

bearcolor = (180, 180, 180)
bordercolor = (0, 0, 0)
floorcolor = (220, 220, 220)
black = (0, 0, 0)
holecolor = (80, 80, 80)
pondcolor = (22, 80, 68)
fishcolor = (109, 195, 178)
fisheyecolor =  (0, 155, 255)
fincolor = (211, 95, 95)

def fish(laysurf, x, y, size, angle):
    surf = pg.Surface((size, size//2), pg.SRCALPHA)
    ellipse(surf, fishcolor, (size*9//34, size*9//68, size*49//68, size*17//68))
    ellipse(surf, bordercolor, (size * 9 // 34, size * 9 // 68, size * 49 // 68, size * 17 // 68), 1)
    circle(surf, fisheyecolor, (size*115/136, size*37//136), size*3//68)
    circle(surf, bordercolor, (size * 115 / 136, size * 37 // 136), size * 3 // 68, 1)
    circle(surf, black, (size * 117 / 136, size * 37 // 136), size // 51)
    polygon(surf, fishcolor, [(size*9//34, size*5//17-size*2//68), (size*3//34, size*29//68-size*2//68), (size*3//68, size*35//136-size*2//68)])
    polygon(surf, bordercolor, [(size * 9 // 34, size * 5 // 17 - size * 2 // 68), (size * 3 // 34, size * 29 // 68 - size * 2 // 68), (size * 3 // 68, size * 35 // 136 - size * 2 // 68)], 1)
    polygon(surf, fincolor, [(size*83//136, size*21//136), (size*107//136, size*11//68), (size*53//68, size*3//34), (size*65//136, size*7//136)])
    polygon(surf, bordercolor, [(size * 83 // 136, size * 21 // 136), (size * 107 // 136, size * 11 // 68), (size * 53 // 68, size * 3 // 34), (size * 65 // 136, size * 7 // 136)], 1)
    polygon(surf, fincolor, [(size*25//34, size*3//8-size//34), (size*13//17, size*8//17-size//34), (size*15//17, size*57//136-size//34), (size*55//68, size*25//68-size//34)])
    polygon(surf, bordercolor, [(size * 25 // 34, size * 3 // 8 - size // 34), (size * 13 // 17, size * 8 // 17 - size // 34), (size * 15 // 17, size * 57 // 136 - size // 34), (size * 55 // 68, size * 25 // 68 - size // 34)], 1)
    polygon(surf, fincolor, [(size*28//68, size*6//17), (size*25//68, size*29//68), (size*69//136, size*61//136), (size*9//17, size*25//68)])
    polygon(surf, bordercolor, [(size * 28 // 68, size * 6 // 17), (size * 25 // 68, size * 29 // 68), (size * 69 // 136, size * 61 // 136), (size * 9 // 17, size * 25 // 68)], 1)
    laysurf.blit(pg.transform.rotate(surf, angle), (x, y))

def bear(x, y, size, orientation):
    surf = pg.Surface((size+100, size+100), pg.SRCALPHA)
    ellipse(surf, bearcolor, (size*23//136, size*23//136, size*15//68, size*2//17))
    ellipse(surf, bordercolor, (size * 23 // 136, size * 23 // 136, size * 15 // 68, size * 2 // 17), 1)
    circle(surf, bearcolor, (size * 27 // 136, size * 27 // 136), size*5//272)
    circle(surf, bordercolor, (size * 27 // 136, size * 27 // 136), size*5//272, 1)
    circle(surf, black, (size*9//34, size*7//34), 4)
    circle(surf, black, (size * 13 // 34, size * 29 // 136), 4)
    line(surf, bordercolor, (size//4, size//4), (size*3/8-size*5//174, size//4+size//174), 1)
    ellipse(surf, bearcolor, (0, size//4, size*43//136, size*77//136))
    ellipse(surf, bordercolor, (0, size // 4, size * 43 // 136, size * 77 // 136), 1)
    ellipse(surf, bearcolor, (size*3//17, size*11//17, size*4//17, size*25//136))
    ellipse(surf, bordercolor, (size * 3 // 17, size * 11 // 17, size * 4 // 17, size * 25 // 136), 1)
    ellipse(surf, bearcolor, (size*43//136, size*27//34, size*3//17, size*9//136))
    ellipse(surf, bordercolor, (size * 43 // 136, size * 27 // 34, size * 3 // 17, size * 9 // 136), 1)
    line(surf, black, (size*45//136, size*69//136), (size*13//34, size*27//68), 5)
    line(surf, black, (size*13//34, size*27//68), (size*53//68, size//17), 5)
    ellipse(surf, bearcolor, (size*9//34, size*3//8, size*19//136, size*9//136))
    ellipse(surf, bordercolor, (size * 9 // 34, size * 3 // 8, size * 19 // 136, size * 9 // 136), 1)
    ellipse(surf, holecolor, (size*75//136, size*83//136, size*3//8, size//8))
    ellipse(surf, bordercolor, (size * 75 // 136, size * 83 // 136, size * 3 // 8, size // 8), 1)
    ellipse(surf, pondcolor, (size*10//17, size*11//17, size*5//17, size*13//136))
    ellipse(surf, bordercolor, (size * 10 // 17, size * 11 // 17, size * 5 // 17, size * 13 // 136), 1)
    line(surf, black, (size * 53 // 68, size // 17), (size * 107 // 136, size * 95 // 136), 2)
    for i in range(randint(2, 5)):
        fish(surf, randint(size*61//136, size*110//136), randint(size*3//4, size*105//136), randint(50, 100), randint(0, 360))
    if orientation == 'right':
        screen.blit(surf, (x, y))
    elif orientation == 'left':
        surf = pg.transform.flip(surf, True, False)
        screen.blit(surf, (x, y))

image = pg.image.load('background.png').convert_alpha()
image = pg.transform.scale(image, (a, b*55//100))
screen.blit(image, (0, 0))
line(screen, bordercolor, (0, b*55//100), (a, b*55//100), 2)
rect(screen, floorcolor, (0, b*55//100+2, a, b-b*55//100-2))
bear(a*7//134, b*50//100, 350, 'right')
bear(a*57//134, b*45//100, 200, 'left')
bear(a*60//154, b*65//100, 300, 'left')
pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()
