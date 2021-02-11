import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix
from utility.gui.scene.top_menu import top_menu

class scene:
    def __init__(self):
        self.top_menu = top_menu()
        self.name = 'scene'
        self.scenes = ['editor','playback','']

    def run(self,event,screen,data):
        val = self.top_menu.update(screen,event)
        if val != None:
            # print(val)
            return val
