import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix

"""
Class for label
"""

class label:
    def __init__(self,text,position):
        pg.init()

        self.text = text
        self.position = position

        self.font = pg.font.Font('freesansbold.ttf', 12)
        self.refresh()

    def refresh(self):
        self.display_text0 = self.font.render(str(self.text).upper(), True, [255,255,255])
        self.textRect0 = self.display_text0.get_rect(center=(self.position.data[0][0], self.position.data[0][1]))

    def render(self,screen):
        screen.blit(self.display_text0, self.textRect0)
