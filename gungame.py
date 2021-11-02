import math
from random import choice
import random
import pygame

while True:
    # PARRAMETERS LIST
    FPS = 30
    screen_width = 1600
    screen_height = 800
    gravity_a = 500
    bomb_a = 50
    classictargets_number = 3
    movingtargets_number = 1
    maxgunpower = 1000
    mingunpower = 400
    powerincreasespeed = 10
    playerscore = 0
    font_name = 'Arial'
    font_size = 50
    indicator_xsize = 10
    indicator_ysize = 100
    tank_xsize = 290
    tank_ysize = 190
    tank_a = 150
    tank_slowa = 75
    maxtank_v = 150
    gun_xsize = 50
    gun_ysize = 30
    gun_centerx = 145
    gun_centery = 50
    gun_r = 35
    maxtargetr = 40
    mintargetr = 10
    playerhealth = 3
    maxmovingtargetv = 300
    minmovingtargetv = 100
    bomberminv = 150
    bombermaxv = 300
    bombnumber = 1
    bombersize = 250
    minbombr = 15
    maxbombr = 30
    quit = False

    # COLOR LIST
    red = 0xFF0000
    blue = 0x0000FF
    yellow = 0xFFC91F
    green = 0x00FF00
    magenta = 0xFF03B8
    cyan = 0x00FFCC
    black = 0x000000
    white = 0xFFFFFF
    grey = 0x7D7D7D
    colors_list = [yellow, green, magenta, cyan]


    class Ball:
        def __init__(self, screen, obj):
            self.screen = screen
            self.x = tank.centerx+(gun_r+gun_xsize)*math.cos(tank.an)
            self.y = tank.centery-(gun_r+gun_xsize)*math.sin(tank.an)
            self.r = 8
            self.vx = 0
            self.vy = 0
            self.color = choice(colors_list)
            self.live = 30
            self.live = True


        def move(self):
            self.vy += gravity_a / FPS
            self.x += self.vx / FPS
            self.y += self.vy / FPS

        def draw(self):
            pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r)

        def hittest(self, obj):
            if (math.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) <= (self.r + obj.r)):
                return True
            else:
                return False

        def bounce(self):
            if (self.x <= self.r) and (self.vx <= 0):
                self.vx = -self.vx * 0.7
            elif (self.x >= screen_width - self.r) and (self.vx >= 0):
                self.vx = -self.vx * 0.7
            elif (self.y <= self.r) and (self.vy <= 0):
                self.vy = -self.vy * 0.7
            elif (self.y >= screen_height - self.r) and (self.vy >= 0):
                self.vy = -self.vy * 0.7

        def disappear(self):
            if (self.y > screen_height - self.r) and (abs(self.vy) < 7.5):
                self.live = False


    class Tank:
        def __init__(self, screen):
            self.screen = screen
            self.x = screen_width*131//320
            self.y = screen_height-tank_ysize
            self.v = 0
            self.keydhold = False
            self.keyahold = False
            self.f2_power = 100
            self.f2_on = 0
            self.color = grey
            self.an = 1
            self.gran = 0
            self.centerx = 0
            self.centery= 0

        def draw(self):
            surf = pygame.Surface((tank_xsize, tank_ysize))
            tank_image = pygame.image.load('tanktexture.png')
            surf.blit(tank_image, (0, 0))
            surf.set_colorkey((255, 255, 255))
            self.screen.blit(surf, (self.x, self.y))

        def speedup(self, event):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.keydhold = True
                elif event.key == pygame.K_a:
                    self.keyahold = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.keydhold = False
                elif event.key == pygame.K_a:
                    self.keyahold = False

        def speeddown(self):
            if self.v > 0:
                self.v -= tank_slowa/FPS
            elif self.v < 0:
                self.v += tank_slowa/FPS

        def move(self):
            if abs(self.v) <= maxtank_v:
                if self.keydhold == True:
                    self.v += tank_a / FPS
                if self.keyahold == True:
                    self.v -= tank_a/FPS
            if not (((self.x < 0) and (self.v < 0)) or ((self.x > screen_width-tank_xsize) and (self.v > 0))):
                self.x += self.v / FPS
            else:
                self.v = 0

        def fire2_start(self):
            self.f2_on = 1

        def fire2_end(self, event):
            global balls, bullet
            bullet += 1
            new_ball = Ball(self.screen, self)
            new_ball.r += 5
            new_ball.vx = self.f2_power * math.cos(-self.an)
            new_ball.vy = self.f2_power * math.sin(-self.an)
            balls.append(new_ball)
            self.f2_on = 0

        def targetting(self, event, obj):
            if event:
                self.an = math.atan2((event.pos[1] - obj.y - gun_centery), (event.pos[0] - obj.x - gun_centerx))
                self.an = -self.an
            if self.f2_on:
                self.color = red
            else:
                self.color = grey

        def draw_gun(self):
            self.gran = self.an/math.pi*180
            self.centery = self.y + gun_centery
            self.centerx = self.x + gun_centerx
            surf = pygame.Surface((gun_xsize + 1, gun_ysize + 1))
            surf.fill((255, 255, 255))
            surf.set_colorkey((255, 255, 255))
            pygame.draw.rect(
                surf,
                self.color,
                (0, 0, gun_xsize, gun_ysize)
            )
            pygame.draw.rect(
                surf,
                black,
                (0, 0, gun_xsize, gun_ysize),
                1
            )
            if (self.gran > 0) and (self.gran <= 90):
                self.screen.blit(pygame.transform.rotate(surf, self.gran), (
                    self.centerx+gun_r*math.cos(self.an)-gun_ysize/2*math.sin(self.an),
                    self.centery-gun_r*math.sin(self.an)-gun_ysize/2*math.cos(self.an)-gun_xsize*math.sin(self.an)
                ))
            elif (self.gran > 90) and (self.gran <= 180):
                self.screen.blit(pygame.transform.rotate(surf, self.gran), (
                    self.centerx+gun_r*math.cos(self.an)+gun_xsize*math.cos(self.an)-gun_ysize/2*math.sin(self.an),
                    self.centery-gun_r*math.sin(self.an)-gun_xsize*math.sin(self.an)+gun_ysize/2*math.cos(self.an)
                ))
            elif (self.gran <= 0) and (self.gran > -90):
                self.screen.blit(pygame.transform.rotate(surf, self.gran), (
                    self.centerx + gun_r * math.cos(self.an) + gun_ysize / 2 * math.sin(self.an),
                    self.centery - gun_r * math.sin(self.an) - gun_ysize / 2 * math.cos(self.an)
                ))
            elif (self.gran <= -90) and (self.gran > -180):
                self.screen.blit(pygame.transform.rotate(surf, self.gran), (
                    self.centerx + gun_r * math.cos(self.an) + gun_ysize / 2 * math.sin(self.an)+gun_xsize*math.cos(self.an),
                    self.centery - gun_r * math.sin(self.an) + gun_ysize / 2 * math.cos(self.an)
                ))


        def power_up(self):
            if self.f2_on:
                if self.f2_power < maxgunpower:
                    self.f2_power += powerincreasespeed
                self.color = red
            else:
                self.f2_power = mingunpower
                self.color = grey

        def draw_indicator(self, x, y):
            pygame.draw.rect(self.screen, grey, (x, y, indicator_xsize, indicator_ysize))
            pygame.draw.rect(self.screen, red, (
            x, y + indicator_ysize - indicator_ysize * (self.f2_power - mingunpower) // (maxgunpower - mingunpower),
            indicator_xsize, indicator_ysize * (self.f2_power - mingunpower) // (maxgunpower - mingunpower)))

    class TargetClassic:
        def __init__(self, screen):
            self.points = 1
            self.screen = screen
            self.x = random.randint(maxtargetr, screen_width-maxtargetr)
            self.y = random.randint(2*font_size+maxtargetr, screen_height-tank_ysize-gun_ysize)
            self.r = random.randint(mintargetr, maxtargetr)
            self.color = red
            self.live = 1

        def new_target(self):
            self.x = random.randint(maxtargetr, screen_width-maxtargetr)
            self.y = random.randint(2*font_size+maxtargetr, screen_height-tank_ysize-gun_ysize)
            self.r = random.randint(mintargetr, maxtargetr)
            self.live = 1

        def draw(self):
            pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r
            )

    class TargetMoving:
        def __init__(self, screen):
            self.points = 5
            self.screen = screen
            self.x = random.randint(maxtargetr, screen_width-maxtargetr)
            self.y = random.randint(2*font_size+maxtargetr, screen_height-tank_ysize-gun_ysize)
            self.r = random.randint(mintargetr, maxtargetr)
            self.color = blue
            self.live = 1
            self.v = random.randint(minmovingtargetv, maxmovingtargetv)

        def new_target(self):
            self.x = random.randint(maxtargetr, screen_width-maxtargetr)
            self.y = random.randint(2*font_size+maxtargetr, screen_height-tank_ysize-gun_ysize)
            self.r = random.randint(mintargetr, maxtargetr)
            self.live = 1

        def draw(self):
            pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r
            )

        def move(self):
            if (((self.x <= self.r) and (self.v < 0)) or ((self.x >= screen_width-self.r) and (self.v > 0))):
                self.v = -self.v
            self.x += self.v/FPS

    class Bomber:
        def __init__(self, screen):
            self.screen = screen
            self.x = 0
            self.y = 20
            self.v = random.randint(bomberminv, bombermaxv)
            self.timer = 0
            self.timedrop = FPS*6

        def draw(self):
            bomber_image = pygame.image.load('bomber.jpg')
            surf = pygame.Surface((512, 512))
            surf.blit(bomber_image, (0, 0))
            surf.set_colorkey((255, 255, 255))
            if (self.v < 0):
                self.screen.blit(pygame.transform.scale(surf, (bombersize, bombersize)), (self.x, self.y))
            else:
                self.screen.blit(pygame.transform.flip(pygame.transform.scale(surf, (bombersize, bombersize)), True, False), (self.x, self.y))

        def move(self):
            if (self.x < 0) and (self.v < 0):
                self.v = random.randint(bomberminv, bombermaxv)
            if (self.x > screen_width-bombersize) and (self.v > 0):
                self.v = random.randint(-bombermaxv, -bomberminv)
            self.x += self.v/FPS

        def bombdrop(self):
            self.timer += 1
            if (self.timer >= self.timedrop):
                bombs.append(Bomb(screen))
                self.timer = 0
                self.timedrop *= 0.95

    class Bomb:
        def __init__(self, screen):
            self.screen = screen
            self.x = bomber.x + bombersize//2
            self.y = bomber.y + bombersize*2//3
            self.v = 0
            self.r = random.randint(minbombr, maxbombr)
            self.color = black
            self.live = True

        def draw(self):
            if self.live:
                pygame.draw.circle(self.screen,
                                   self.color,
                                   (self.x, self.y),
                                   self.r
                                   )

        def move(self):
            self.v += bomb_a/FPS
            self.y += self.v/FPS

        def hittest(self, obj):
            if ((self.y+self.r>=screen_height-tank_ysize) and (self.x+self.r>=obj.x) and (self.x+self.r<=obj.x+tank_xsize) and self.live):
                return True
            else:
                return False

        def disappear(self):
            if (self.y+self.r>screen_height):
                self.live = False

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    game_font = pygame.font.SysFont(font_name, font_size)
    text_health = game_font.render(str(playerhealth), True, black)
    bullet = 0
    balls = []
    classictargets = []
    movingtargets = []
    bombs = []
    clock = pygame.time.Clock()
    bomber = Bomber(screen)
    tank = Tank(screen)
    for i in range(classictargets_number):
        classictargets.append(TargetClassic(screen))
    for i in range(movingtargets_number):
        movingtargets.append(TargetMoving(screen))
    finished = False

    while not finished:
        if playerhealth <= 0:
            finished = True
        screen.fill(white)
        for t in classictargets:
            t.draw()
        for m in movingtargets:
            m.move()
            m.draw()
        for l in bombs:
            if l.live:
                l.move()
                l.draw()
                l.disappear()
                if l.hittest(tank):
                    l.live = False
                    playerhealth -= 1
        tank.draw()
        tank.draw_indicator(tank.x, tank.y)
        tank.speeddown()
        bomber.move()
        tank.move()
        tank.draw_gun()
        for b in balls:
            b.disappear()
            if b.live:
                b.draw()
                b.move()
                b.bounce()
        bomber.draw()
        bomber.bombdrop()
        text_score = game_font.render('Score: ' + str(playerscore), True, black)
        text_health = game_font.render('Health: ' + str(playerhealth), True, black)
        screen.blit(text_score, (0, 0))
        screen.blit(text_health, (0, font_size))
        pygame.display.update()

        clock.tick(FPS)
        for event in pygame.event.get():
            tank.speedup(event)
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                tank.fire2_start()
            elif event.type == pygame.MOUSEBUTTONUP:
                tank.fire2_end(event)
            elif event.type == pygame.MOUSEMOTION:
                tank.targetting(event, tank)

        for b in balls:
            for t in classictargets:
                if b.hittest(t) and t.live and b.live:
                    t.live = 0
                    playerscore += t.points
                    t.new_target()
            for m in movingtargets:
                if b.hittest(m) and m.live and b.live:
                    m.live = 0
                    playerscore += m.points
                    m.new_target()

        tank.power_up()

    finalmenu = True
    while finalmenu:
        screen.fill(white)
        text_finalscore = game_font.render('Your final score: ' + str(playerscore), True, black)
        text_restart = game_font.render('To restart press Space', True, black)
        text_quit = game_font.render('To quit press ESC', True, black)
        screen.blit(text_finalscore, (screen_width*3//8, screen_height//3))
        screen.blit(text_restart, (screen_width*11//32, screen_height*2//3))
        screen.blit(text_quit, (screen_width*3//8, screen_height*2//3+font_size))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
                finalmenu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit = True
                    finalmenu = False
                if event.key == pygame.K_SPACE:
                    finalmenu = False

    if quit == True:
        break
pygame.quit()
