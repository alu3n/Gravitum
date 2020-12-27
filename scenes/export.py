import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix
from template.scene import scene

class export(scene):
    def __init__(self):
        super().__init__()

    def run(self,event,screen,data):
        screen.fill([0,217,0])

        return(super().run(event,screen,data))
