import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix
from utility.gui.button import button

"""
This class is used to represent buttons in left solvers menu in the editor scene
"""

class menu_solvers:
    def __init__(self):
        self.width = 300
        self.item_height = 30
        self.bg = (1,1,1,1)

    def update_items(self,data,selected):
        self.items = [x.type for x in data.solvers]
        self.buttons = []
        for x in range(len(self.items)):
            if x != selected:
                self.buttons.append(button(self.items[x],Matrix([[self.width,self.item_height]]),Matrix([[0,0]]),x,font_size=14,color_passive=[55,55,55]))
            else:
                self.buttons.append(button(self.items[x],Matrix([[self.width,self.item_height]]),Matrix([[0,0]]),x,font_size=14,color_passive=[111,111,111]))



    def update_buttons(self,screen):
        for x in range(len(self.buttons)):
            self.buttons[x].position = Matrix([[150,55+x*self.item_height]])

    def update(self,event,screen,data,selected):
        self.update_items(data,selected)
        self.update_buttons(screen)
        self.bg = (0,0,self.width,screen.get_size()[1])
        pg.draw.rect(screen,[14,14,14],self.bg)
        rtrval = None
        for x in self.buttons:
            val = x.update(screen, event)
            if val != None:
                rtrval = val
        return rtrval
