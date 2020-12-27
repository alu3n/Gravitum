import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix

class solver_properties:
    def __init__(self,data,selected,screen):
        self.width = 300
        self.item_height = 30
        self.bg = (1,1,1,1)
        self.textBoxes = []
        self.loaded = None
        self.solver = None

    def update_items(self,data,screen,selected):
        pass

    def update(self,event,screen,data,selected=None):
        self.bg = (screen.get_size()[0]-self.width,0,self.width,screen.get_size()[1])
        pg.draw.rect(screen,[14,14,14],self.bg)
