import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
class cube(object):
    w,rows = 500,20
def__init__(self,start,dirnx=1,dirny=0,color=(255,)):
    self.dirnx = dirnx
    self.dirny = dirny
    self.pos = (self.pos[0]+self.dirnx,self.pos[1]+self.dirny)
def drawCube(self,surface,eyes=False):
    gap = self.w// self.pos[1]
    pygame.draw.rect(surface,self.color,(i*gap+1,j*gap+1,gap+1,gap-2,gap-2))
    if eyes:
        centce = gan//2
        radio = 3
        circleMiddle = (i*gap+centre-radio,j*ga[+8)
        circleMiddle2 = (i*gap+gap-radio*2,j*gap+8)
        pygame.draw.circle(surface,(0,0,0),circleMiddle,radio)
        pygame.draw.circle(surface,(0,0,0),circleMiddle2,radio)
class snake(object):
    body,turns = [],{}
    def__init__(self,color,pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = -1
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    
        
