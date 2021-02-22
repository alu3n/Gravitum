import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())


"""
Function for displaying editor information cluster (scale and position)
"""

class editor_info:
    def __init__(self):
        self.font = pg.font.Font('freesansbold.ttf', 16)

    def update(self,screen, scale, position_):
        scale = self.font.render('Scale: {}'.format(scale), True, [255,255,255])
        position = self.font.render('Position: {}'.format(position_), True, [255,255,255])

        position_rect = position.get_rect(center=(screen.get_size()[0]/2,60))
        scale_rect = scale.get_rect(center=(screen.get_size()[0]/2,80))
        screen.blit(position, position_rect)
        screen.blit(scale, scale_rect)
