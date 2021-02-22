import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix
from utility.gui.elements.textbox import textbox
from utility.gui.elements.label import label


"""
This class is made to proceduraly create menu that contains all the solver properties
"""

class textbox_cluster:
    def __init__(self):
        self.loaded = False

    def load(self,data,selected):
        self.loaded = True

        self.data = data
        self.selected = selected

        self.buttons = []
        for x in self.data.solvers[selected].attributes:
            temp = []
            for y in range(len(self.data.solvers[selected].attributes[x].data[0])):
                temp.append(textbox(300/len(self.data.solvers[selected].attributes[x].data[0]),20,self.data.solvers[selected],x,y))
            self.buttons.append(temp)

    def unload(self):
        self.loaded = False

    def refresh(self,screen,event):
        v = 70
        self.labels = []
        rtv = None
        for x in self.buttons:
            self.labels.append(label(x[0].parameter,Matrix([[screen.get_size()[0]-150,v-20]])))

            w = 0
            for y in x:
                val = y.update(screen,Matrix([[screen.get_size()[0]-300+(300/len(x))/2+w,v]]),event)
                if val != None:
                    rtv = val
                w += 300/len(x)
            v += 40
            w = 0
        for x in self.labels:
            x.render(screen)
        if rtv != None:
            for x in self.buttons:
                for y in x:
                    if y != rtv:
                        y.selected = False



    def update(self,screen,data,event):
        if self.loaded:
            self.refresh(screen,event)
