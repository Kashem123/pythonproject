from tkinter import*
#intialize the pygame
pygame.init()

#creat the screen
screen = pygame.display.set_mode((800,600))
#Title and Icon
pygame.display.set_caption("Space.invaders")
icon = pygame.image.load("")###pic ar link dita hoba string
pygame.display.set_icon(icon)
#game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            running = False
    #RGB - Red,Green,Blue
    screen.fill(255,0,0))
    pygame.display.update()