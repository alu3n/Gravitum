import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix

from simulation.forces.gravity import gravity
from simulation.forces.drag import drag
from simulation.forces.source import source
from simulation.forces.noise import noise
from simulation.forces.vortex import vortex

from utility.gui.button import button

class add_remove:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.items = ['add','remove']
        self.buttons = []
        for x in range(len(self.items)):
            self.buttons.append(button(self.items[x],Matrix([[self.width/2,self.height]]),Matrix([[200,200]]),self.items[x],font_size=15))

    def update_buttons(self,screen):
        for x in range(len(self.buttons)):
            self.buttons[x].position = Matrix([[self.width/len(self.items)/2+self.width/len(self.items)*x,screen.get_size()[1]-self.height/2]])

    def render(self,screen):
        pass

    def update(self,event,screen):
        self.render(screen)
        self.update_buttons(screen)
        rtrval = None
        for x in self.buttons:
            val = x.update(screen, event)
            if val != None:
                rtrval = val
        return rtrval

    def run(self,event,screen):
        pass
