import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix

class player:
    def __init__(self,data):
        self.frame = 0
        self.max_frame = len(data)
        self.data = data

    def next(self,screen,camera):
        for x in self.data[self.frame%self.max_frame]:
            center = [camera.x+x[0][0]*camera.scale,camera.y+x[0][1]*camera.scale]
            pg.draw.circle(screen,x[1],center,x[2]*camera.scale)
        self.frame += 1

# pg.draw.circle(screen,[0,0,0],center,1*camera.scale*size)
