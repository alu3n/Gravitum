import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

"""
Function for displaying frame
"""

def display_frame(screen, frame, text):
    pg.init()
    font = pg.font.Font('freesansbold.ttf', 30)
    display_text = font.render('{} frame: {}'.format(text,frame), True, [255,255,255])
    textRect = display_text.get_rect(center=(screen.get_size()[0]/2, screen.get_size()[1]/2))
    screen.fill([0,0,0])
    screen.blit(display_text, textRect)
    pg.display.flip()
