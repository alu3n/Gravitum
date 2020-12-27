import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix
from utility.gui.button import button

class add_popup:
    def __init__(self):
        self.width = 200
        self.item_height = 30

        self.items = ['source','drag','gravity','noise','vortex','attract','cancel']
        self.buttons = []
        for x in range(len(self.items)):
            self.buttons.append(button(self.items[x],Matrix([[self.width,self.item_height]]),Matrix([[0,0]]),self.items[x],font_size=14))

    def update_buttons(self,screen):
        for x in range(len(self.buttons)):
            self.buttons[x].position = Matrix([[screen.get_size()[0]/2,screen.get_size()[1]/2-self.item_height*len(self.items)/2+self.item_height/2+x*self.item_height]])

    def update(self,event,screen):
        self.update_buttons(screen)
        rtrval = None
        for x in self.buttons:
            val = x.update(screen, event)
            if val != None:
                rtrval = val
        return rtrval
