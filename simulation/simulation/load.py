import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())


from utility.mathematics.matrix import Matrix
from utility.gui.button import button

class load:
    def __init__(self):
        self.button = button('simulate',Matrix([[150,50]]),Matrix([[100,30]]),'simulate',font_size=20)

    def update_button(self,screen,event):
        self.button.position = Matrix([[screen.get_size()[0]/2,screen.get_size()[1]-50]])
        val = self.button.update(screen, event)
        return val

    def update(self, screen, event):
        val = self.update_button(screen,event)
        if val != None:
            # print(val)
            return val
