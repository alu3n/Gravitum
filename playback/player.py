import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix

from utility.gui.elements.display_info import display_info

class player:
    def __init__(self,data):
        self.frame = 0
        self.max_frame = len(data)
        self.data = data
        self.display_info = display_info()

    def next(self,screen,camera):
        for x in self.data[self.frame%self.max_frame]:
            center = [camera.x+x[0][0]*camera.scale,camera.y+x[0][1]*camera.scale]
            pg.draw.circle(screen,x[1],center,x[2]*camera.scale)
            self.display_info.update(screen,self.frame%self.max_frame,camera.scale,[camera.offsetx,camera.offsety])
        self.frame += 1
