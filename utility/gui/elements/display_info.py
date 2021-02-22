import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

"""
Function for displaying information cluster (Frame,position,scale)
"""

class display_info:
    def __init__(self):
        self.font = pg.font.Font('freesansbold.ttf', 16)

    def update(self,screen, frame, scale, position):
        frame = self.font.render('Frame: {}'.format(frame), True, [255,255,255])
        position = self.font.render('Position: {}'.format(position), True, [255,255,255])
        scale = self.font.render('Scale: {}'.format(scale), True, [255,255,255])

        frame_rect = frame.get_rect(center=(100,screen.get_size()[1]/2+20))
        position_rect = position.get_rect(center=(100,screen.get_size()[1]/2))
        scale_rect = scale.get_rect(center=(100,screen.get_size()[1]/2-20))
        screen.blit(frame, frame_rect)
        screen.blit(position, position_rect)
        screen.blit(scale, scale_rect)
