# USED LIBRARIES
import pygame
from pygame.draw import *
from random import randint
import math

# LIST OF PARAMETERS
gametime = ''
FPS = 30
ball_points = 1
square_points = 5
screen_xsize = 1200
screen_ysize = 900
font_size = 50
# BALL PARAMETERS
ball_number = 5
maxball_r = 50
minball_r = 30
maxball_V = 200
minball_V = 50
# SQUARE PARAMETERS
square_number = 2
minsquare_size = 35
maxsquare_size = 50
minsquare_V = 200
maxsquare_V = 250
# DEFINITIONS
timedelta = 1 / FPS
player_score = 0
timecounter = 0
# BALL DEFINITIONS
ball_r = [None] * ball_number
ball_x = [None] * ball_number
ball_y = [None] * ball_number
ball_Vx = [None] * ball_number
ball_Vy = [None] * ball_number
ball_color = [None] * ball_number
# SQUARE DEFINITIONS
square_size = [None] * square_number
square_x = [None] * square_number
square_y = [None] * square_number
square_Vx = [None] * square_number
square_Vy = [None] * square_number
square_color = [None] * square_number

# LIST OF COLORS
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
black = (0, 0, 0)
white = (255, 255, 255)
backgroundcolor = (200, 200, 240)
colors = [red, blue, yellow, green, magenta, cyan]


# RANDOM NEW BALL PARAMETERS
def ball_create(i):
    ball_x[i] = randint(2 * maxball_r, screen_xsize - 2 * maxball_r)
    ball_y[i] = randint(2 * maxball_r, screen_ysize - 2 * maxball_r)
    ball_r[i] = randint(minball_r, maxball_r)
    ball_color[i] = colors[randint(0, len(colors) - 1)]
    ball_Vx[i] = randint(-maxball_V, maxball_V)
    ball_Vy[i] = randint(-maxball_V, maxball_V)


# RANDOM NEW SQUARE PARAMETERS
def square_create(i):
    square_x[i] = randint(maxsquare_size, screen_xsize - maxsquare_size)
    square_y[i] = randint(maxsquare_size, screen_ysize - maxsquare_size)
    square_size[i] = randint(minsquare_size, maxsquare_size)
    square_color[i] = colors[randint(0, len(colors) - 1)]
    square_Vx[i] = randint(-maxsquare_V, maxsquare_V)
    square_Vy[i] = randint(-maxsquare_V, maxsquare_V)


# DRAW A BALL
def ball_draw(i):
    circle(screen, ball_color[i], (ball_x[i], ball_y[i]), ball_r[i])
    circle(screen, black, (ball_x[i], ball_y[i]), ball_r[i], 1)


# DRAW A SQUARE
def square_draw(i):
    rect(screen, square_color[i], (square_x[i], square_y[i], square_size[i], square_size[i]))
    rect(screen, black, (square_x[i], square_y[i], square_size[i], square_size[i]), 1)


# BALL REFLECTION FROM THE WALLS
def ball_wallbounce(i):
    if (ball_x[i] < ball_r[i]) and (ball_Vx[i] < 0):
        ball_Vx[i] = randint(minball_V, maxball_V)
    elif (ball_x[i] > screen_xsize - ball_r[i]) and (ball_Vx[i] > 0):
        ball_Vx[i] = randint(-maxball_V, -minball_V)
    elif (ball_y[i] < ball_r[i]) and (ball_Vy[i] < 0):
        ball_Vy[i] = randint(minball_V, maxball_V)
    elif (ball_y[i] > screen_ysize - ball_r[i]) and (ball_Vy[i] > 0):
        ball_Vy[i] = randint(-maxball_V, -minball_V)


# SQUARE REFLECTION FROM THE WALLS
def square_wallbounce(i):
    if (square_x[i] < 0) and (square_Vx[i] < 0):
        square_Vx[i] = randint(minsquare_V, maxsquare_V)
    elif (square_x[i] > screen_xsize - square_size[i]) and (square_Vx[i] > 0):
        square_Vx[i] = randint(-maxsquare_V, minsquare_V)
    elif (square_y[i] < 0) and (square_Vy[i] < 0):
        square_Vy[i] = randint(minsquare_V, maxsquare_V)
    elif (square_y[i] > screen_ysize - square_size[i]) and (square_Vy[i] > 0):
        square_Vy[i] = randint(-maxsquare_V, minsquare_V)


# CHECK BALL HIT
def ball_hitcheck(event, i):
    if (math.sqrt((event.pos[0] - ball_x[i]) ** 2 + (event.pos[1] - ball_y[i]) ** 2) <= ball_r[i]):
        return True
    else:
        return False


# CHECK SQUARE HIT
def square_hitcheck(event, i):
    if (event.pos[0] >= square_x[i]) and (event.pos[0] <= square_x[i] + square_size[i]) and (
            event.pos[1] >= square_y[i]) and (event.pos[1] <= square_y[i] + square_size[i]):
        return True
    else:
        return False


# CREATING OBJECTS
pygame.init()
pygame.font.init()
game_font = pygame.font.SysFont('Arial', font_size)
screen = pygame.display.set_mode((screen_xsize, screen_ysize))
screen.fill(backgroundcolor)
pygame.display.update()
clock = pygame.time.Clock()
game_ended = False
game_started = False


#START MENU
#TEXT
text_titlesurface = game_font.render('Ultimate Ball Clicking Game', True, black)
text_rulessurface1 = game_font.render('Click as much figures as you can!', True, black)
text_rulessurface2 = game_font.render("You'll get 1 point for each circle", True, black)
text_rulessurface3 = game_font.render("and 5 points for each square you clicked.", True, black)
text_startsurface1 = game_font.render('To start, enter the game time in seconds', True, black)
text_startsurface2 = game_font.render('and press Enter:', True, black)
#TITLE
screen.blit(text_titlesurface, (screen_xsize*4//15, 0))
#RULES
screen.blit(text_rulessurface1, (screen_xsize*3//15, screen_ysize * 2 // 5 + 3 * font_size + 30))
screen.blit(text_rulessurface2, (screen_xsize*7//30, screen_ysize * 2 // 5 + 4 * font_size + 40))
screen.blit(text_rulessurface3, (screen_xsize*2//15, screen_ysize * 2 // 5 + 5 * font_size + 50))
#ENTER
screen.blit(text_startsurface1, (screen_xsize*2//15, screen_ysize//5))
screen.blit(text_startsurface2, (screen_xsize//3+20, screen_ysize//5+font_size+10))
rect(screen, white, (screen_xsize*9//24, screen_ysize//5+2*font_size+30, 300, 50))
rect(screen, black, (screen_xsize*9//24, screen_ysize//5+2*font_size+30, 300, 50), 1)
pygame.display.update()
#INPUTBOX
while not game_started:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_started = True
            game_ended = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_started = True
            if event.key == pygame.K_BACKSPACE:
                gametime = gametime[:-1]
            else:
                gametime += event.unicode
        rect(screen, white, (screen_xsize * 9 // 24, screen_ysize // 5 + 2 * font_size + 30, 300, 50))
        rect(screen, black, (screen_xsize * 9 // 24, screen_ysize // 5 + 2 * font_size + 30, 300, 50), 1)
        input_surface = game_font.render(gametime, True, black)
        screen.blit(input_surface, (screen_xsize*9//24, screen_ysize//5+2*font_size+30))
        pygame.display.update()


#LOADING SCREEN (AND I KNOW ITS BAD)
text_loadsurface = game_font.render('The game will start in...', True, black)
text_countdownsurface3 = game_font.render('3', True, black)
text_countdownsurface2 = game_font.render('2', True, black)
text_countdownsurface1 = game_font.render('1', True, black)
clock.tick(1)
screen.fill(backgroundcolor)
screen.blit(text_loadsurface, (screen_xsize*4//15, screen_ysize//5))
screen.blit(text_countdownsurface3, (screen_xsize//2-10, screen_ysize//5+font_size+1))
pygame.display.update()
clock.tick(1)
screen.fill(backgroundcolor)
screen.blit(text_loadsurface, (screen_xsize*4//15, screen_ysize//5))
screen.blit(text_countdownsurface2, (screen_xsize//2-10, screen_ysize//5+font_size+1))
pygame.display.update()
clock.tick(1)
screen.fill(backgroundcolor)
screen.blit(text_loadsurface, (screen_xsize*4//15, screen_ysize//5))
screen.blit(text_countdownsurface1, (screen_xsize//2-10, screen_ysize//5+font_size+1))
pygame.display.update()
clock.tick(1)


#STARTING OBJECTS
gametime = int(gametime)
timer = FPS * gametime
for i in range(ball_number):
    ball_create(i)
    ball_draw(i)
for i in range(square_number):
    square_create(i)
    square_draw(i)


#GAME SECTION
while not game_ended:
    clock.tick(FPS)
    #TIMER
    timecounter += 1
    if (timecounter >= timer):
        game_ended = True
    #OBJECT PROCESSING
    for i in range(ball_number):
        ball_wallbounce(i)
        ball_x[i] += ball_Vx[i] * timedelta
        ball_y[i] += ball_Vy[i] * timedelta
        ball_draw(i)
    for i in range(square_number):
        square_wallbounce(i)
        square_x[i] += square_Vx[i] * timedelta
        square_y[i] += square_Vy[i] * timedelta
        square_draw(i)
    #TEXT PROCESSING
    text_infosurface = game_font.render('Score: ' + str(player_score) + '               Time remaining: ' + str(gametime-timecounter//30), False, black)
    screen.blit(text_infosurface, (0, 0))
    pygame.display.update()
    #EVENT PROCESSING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_ended = True
        elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
            for i in range(ball_number):
                if ball_hitcheck(event, i) == True:
                    player_score += ball_points
                    ball_create(i)
            for i in range(square_number):
                if square_hitcheck(event, i) == True:
                    player_score += square_points
                    square_create(i)
    screen.fill(backgroundcolor)


#RESULTS
while game_ended:
    screen.fill(backgroundcolor)
    text_resultssurface = game_font.render('Your final score is:', True, black)
    text_finalscoresurface = game_font.render(str(player_score), True, black)
    text_congratulationsurface = game_font.render('Good job!', True, black)
    text_exitsurface = game_font.render('Press Enter to exit', True, black)
    screen.blit(text_resultssurface, (screen_xsize*5//15, screen_ysize//5))
    screen.blit(text_finalscoresurface, (screen_xsize//2-10, screen_ysize//5+font_size+10))
    screen.blit(text_congratulationsurface, (screen_xsize*25//60, screen_ysize//5+2*font_size+20))
    screen.blit(text_exitsurface, (screen_xsize*10//30, screen_ysize*4//5))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pygame.quit()