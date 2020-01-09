import random
import math
import pygame
from pygame import mixer



pygame.init()

screen = pygame.display.set_mode((900, 600))
background = pygame.image.load('mountain (1).png')
mixer.music.load('background.wav')
mixer.music.play(-1)

pygame.display.set_caption("GAME OF THRONES: THE TARGAREYAN ERA")

icon = pygame.image.load('dragon (1).png')
pygame.display.set_icon(icon)

object1 = pygame.image.load('castle.png')
objectx = 0
objecty = 470

obj2 = pygame.image.load('castle.png')
objx = 770
objy = 470

player1img = pygame.image.load('knight.png')
player1x = 400
player1y = 500
player1x_change = 0

player2img = []
player2x = []
player2y = []
player2x_change = []
player2y_change = []
no_of_enemies = 7

for i in range(no_of_enemies):
    player2img.append(pygame.image.load('dragon (3).png'))
    player2x.append(random.randint(0, 835))
    player2y.append(random.randint(50, 150))
    player2x_change.append(0.3)
    player2y_change.append(40)

sword = pygame.image.load('sword (1).png')
swordx = 0
swordy = 500
swordx_change = 0
swordy_change = 5
sword_state = "ready"

score_value = 0
font = pygame.font.Font('Angelina sans.ttf',52)

textx = 10
texty = 10

instx = 9
insty = 40

terx = 10
tery = 60

creax = 400
creay = 560

over = pygame.font.Font('Angelina Alt Demo.ttf', 54)

instructions = pygame.font.Font('freesansbold.ttf', 15)

start_and_stop = pygame.font.Font('freesansbold.ttf', 13)

credit = pygame.font.Font('Angelina Alt Demo.ttf', 40)

def creator(x,y):
    creartors = credit.render("A Game By Remin Franklin",True , (0, 0, 0))
    screen.blit(creartors, (x,y))

def terminator(x,y):
    button = start_and_stop.render("press SPACE to shoot or Q to quit",True, (225, 225, 225))
    screen.blit(button, (x,y))

def show_instructions(x,y):
    instructions_sh = instructions.render(" USE left arrow and right arrow to move the king",True, (255, 255, 255))
    screen.blit(instructions_sh, (x,y))

def show_score(x,y):
    score = font.render("score: " + str(score_value),True, (255,255,255))
    screen.blit(score, (x,y))

def game_over_text():
    over_text = over.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (300, 300))
def object(x,y):
    screen.blit(object1, (x,y))
def obj(x,y):
    screen.blit(obj2, (x,y))

def player1(x,y):
    screen.blit(player1img, (x,y))
def player2(x,y, i):
    screen.blit(player2img[i], (x,y))
def swing_sword(x,y):
    global sword_state
    sword_state = "swing"
    screen.blit(sword, (x+16,y+10))

def isCollision(player2x, player2y, swordx, swordy):
    distance = math.sqrt((math.pow(player2x-swordx,2)) + (math.pow(player2y-swordy,2)))
    if distance < 27:
        return True
    else:
        return False

running = True
while running:
    screen.fill((52, 100, 55))
    screen.blit(background, (210, 140))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            player1x_change = -2
        if event.key == pygame.K_d:
            player1x_change = 2
        if event.key == pygame.K_ENTER:
            if sword_state is "ready":
                sword_sound = mixer.Sound('laser.wav')
                sword_sound.play()
                swordx = player1x
                swing_sword(player1x,swordy)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.key == pygame.MOUSEWHEEL:
                sword_sound = mixer.Sound('laser.wav')
                sword_sound.play()
                swordx = player1x
                swing_sword(player1x, swordy)
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            player1x_change = 0

    player1x += player1x_change
    if player1x <= 110:
        player1x = 110
    elif player1x >= 710:
        player1x = 710

    for i in range(no_of_enemies):
        if player2y[i] > 200:
            for j in range(no_of_enemies):
                player2y[j] = 2000
            game_over_text()
            break

        player2x[i] += player2x_change[i]
        if player2x[i] <= 0:
            player2x_change[i] = 0.3
            player2y[i] += player2y_change[i]
        elif player2x[i] >= 836:
            player2x_change[i] = -0.3
            player2y[i] += player2y_change[i]
        collision = isCollision(player2x[i], player2y[i], swordx, swordy)
        if collision:
            collision_sound = mixer.Sound('explosion.wav')
            collision_sound.play()
            swordy = 480
            sword_state = "ready"
            score_value += 1
            player2x[i] = random.randint(0, 900)
            player2y[i] = random.randint(50, 150)
        player2(player2x[i], player2y[i], i)
    if swordy <= 0:
        swordy = 500
        sword_state = "ready"
    if sword_state is "swing":
        swing_sword(player1x, swordy)
        swordy -= swordy_change


    player1(player1x,player1y)
    show_score(textx, texty)
    show_instructions(instx, insty)
    terminator(terx, tery)
    creator(creax, creay)
    object(objectx, objecty)
    obj(objx, objy)
    pygame.display.update()