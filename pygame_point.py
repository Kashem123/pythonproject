import pygame
import math
import random
from pygame import mixer

pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#background downlad kora img dita hoba
background = pygame.image.load("")

#background sound
mixer.music.load("")
mixer.music.play(-1)

# title and icon
pygame.display.set_caption("Space Invaders")

#icon download diya file show korta hoba
icon = pygame.image.load("")
pygame.display.set_icon(icon)

#player img download kora link dita hoba
player_img = pygame.image.load("")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemy_Img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemy_Img.append(pygame.image.load(""))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#Billet
bullet_Img = pygame.image.load("")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 40
bullet_state = "ready"

#score

score_value = 0
font = pygame.font.Font("freesansold.ttf",32)

textX = 10
textY = 10

# game orver text
over_font = pygame.font.Font("",64)
def show_score(x,y):
    score = font.render("Score:"+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text(x,y):
    over_text = over_font.render("Game over",True,(255,255,255))
    screen.blit(over_text,(200,250))

def player(x,y):
    screen.blit(player_img,(x,y))

def enemy(x,y,i):
    screen.blit(enemy_Img[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_Img,(x+16 , y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY - bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

#Game loop
running = True
while running:
    # FGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background,(0, 0))

    for event in pygame.event.get():
        if event.type == pygame.quit():
            running = False

    # if keystroke is pressed check whether its right of left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # 5 = 5 + (-0.1) -> 5 = 5 - 0.1
    # 5 = 5 - 0.1

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
#enemy movemont
    for i in range(num_of_enemies):

        # Game is over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]

        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
#bullate movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    #collation
    collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)

    if collision:
        explosion_sound = mixer.sound("")
        explosion_sound.play()
        bulletY = 480
        bullet_state = "ready"
        score_value += 1
        print(score_value)
        enemyX[i] = random.randint(0, 800)
        enemyY[i] = random.randint(50, 150)

    enemy(enemyX[i], enemyY[i],i)
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()


