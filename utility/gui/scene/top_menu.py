import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix
from utility.gui.button import button

class top_menu:
    def __init__(self):
        self.height = 40
        self.items = ['editor','playback','export']
        self.buttons = []
        for x in range(len(self.items)):
            self.buttons.append(button(self.items[x],Matrix([[100,25]]),Matrix([[100+x*100,100]]),self.items[x]))

    def update_buttons(self,screen):
        for x in range(len(self.buttons)):
            self.buttons[x].size = Matrix([[screen.get_size()[0]/len(self.buttons),self.height]])
            self.buttons[x].position = Matrix([[screen.get_size()[0]/len(self.buttons)/2+screen.get_size()[0]/len(self.buttons)*x,self.height/2]])

    def update(self, screen, event):
        self.update_buttons(screen)
        for x in self.buttons:
            val = x.update(screen, event)
            if val != None:
                return val
