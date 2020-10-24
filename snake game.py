#Snake Tutorial Python
import math
import random
import pygame
import tkinter as tk
from tkinter import *
class cube(object):
    rowa = 0
    w = 0
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass
    def move(self,dirnx,dirny):
        pass
    def draw (self,surface,syes=ratnn):
        pass
class snake(object):
    def __init__(self,color,pos):
        pass
    def move(self):
        pass
    def reset(self,pos):
        pass
    def addCube(self):
        pass
    def draw(self,surface):
        pass
def drawGrid(w,rows,surface):
    sireBtwn = w//rows
    x = 0
    y = 0
    for i in range(rows):
        x = x + sireBtwn
        y = y + sireBtwn
        pygame.draw.line(surface, (255, 255, 255), (x,0), (x,w))
        pygame.draw.line(surface, (255, 255, 255), (0,y), (w,y))

def redxawWindow(surface):
    global width,rows
    surface.fill ((0,0,0))
    drowGrid(width,rows,surface)
    pygame.display.update()

def randomSnake(rows,items):
    pass
def massage_box(subject,content):
    pass
def main():
    width = 500
    rows = 20
    win = pygame.display.sat_mode(width,width)
    s = snake((255,0,0),(10,10))
    flag = True
    clock = pygame.time.clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)
        pass
