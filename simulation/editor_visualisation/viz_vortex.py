import os
import sys
import pygame as pg

"""
This file takes care of vortex force visualisation.
Based on user specified parameters the function renders graphics on screen
that should help user to better imagine how would his simulation look like.
"""

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix

def viz_vortex(pos,camera,screen,size,speed):

    center = [camera.x+pos[0]*camera.scale,camera.y+pos[1]*camera.scale]

    l0 = Matrix([[center[0],center[1]-size*camera.scale]])
    l1 = Matrix([[center[0]+camera.scale*speed,center[1]-size*camera.scale]])

    for x in range(12):
        l0.rotate(360/12,center)
        l1.rotate(360/12,center)
        pg.draw.line(screen, [255,0,0], l0.data[0],l1.data[0])


    pg.init()
    font = pg.font.Font('freesansbold.ttf', int(camera.scale*1.5))

    text = font.render('Vortex', True, [255,255,255])
    textRect = text.get_rect(center=(center[0],center[1]))
    screen.blit(text, textRect)
