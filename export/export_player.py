import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.gui.elements.display_info import display_info

from utility.mathematics.matrix import Matrix

class player:
    def __init__(self,data):
        self.frame = 0
        self.max_frame = len(data)
        self.data = data
        self.display_info = display_info()

    def next(self,screen,camera,size):
        m0 = size[0]/screen.get_size()[0]
        m1 = size[1]/screen.get_size()[1]
        mult = m0*m1
        # print('x')
        for x in self.data[self.frame%self.max_frame]:
            self.display_info.update(screen,self.frame%self.max_frame,camera.scale,[camera.offsetx,camera.offsety])
            center = [camera.x+x[0][0]*camera.scale/mult,camera.y+x[0][1]*camera.scale/mult]
            pg.draw.circle(screen,x[1],center,x[2]*camera.scale/mult)
        self.frame += 1
