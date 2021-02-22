import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix

"""
Class that is made to represent button
"""

class button:
    def __init__(self,text,size,position,return_value,font_size=20,font_color=[217,217,217],color_passive=[38,38,38],color_active=[70,130,180]):
        pg.init()

        self.text = text
        self.size = size
        self.position = position
        self.return_value = return_value

        self.font_size = font_size
        self.font_color = font_color
        self.color_passive = color_passive

        ### temporarily disabled and changed for passive
        self.color_active = color_passive

        self.active = False

        self.refresh()

    def refresh(self):

        self.font = pg.font.Font('freesansbold.ttf', self.font_size)
        # self.font = pg.font.Font('freesans.ttf',self.font_size)
        self.display_text = self.font.render(self.text.upper(), True, self.font_color)
        self.rect = pg.Rect(self.position.data[0][0]-self.size.data[0][0]/2,self.position.data[0][1]-self.size.data[0][1]/2, self.size.data[0][0], self.size.data[0][1])
        self.textRect = self.display_text.get_rect(center=(self.position.data[0][0], self.position.data[0][1]))

    def render(self,screen):
        if self.active:
            pg.draw.rect(screen, self.color_active,self.rect)
        else:
            pg.draw.rect(screen, self.color_passive,self.rect)
        screen.blit(self.display_text, self.textRect)


    def update(self, screen, event):
        self.refresh()
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.active = True
        else:
            self.active = False
        if event != None:
            if event.type == pg.MOUSEBUTTONDOWN and self.active:
                self.render(screen)
                return self.return_value
        self.render(screen)
