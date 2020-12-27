import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix

def viz_vortex(pos,camera,screen,size,speed):

    center = [camera.x+pos[0]*camera.scale,camera.y+pos[1]*camera.scale]


    # pg.draw.line(screen, [0,0,0], center, [l0.data[0][0],l0.data[0][1]],2)
    # pg.draw.line(screen, [0,0,0], center, [l1.data[0][0],l1.data[0][1]],2)
    # pg.draw.line(screen, [25,25,25], center, [l2.data[0][0],l2.data[0][1]],2)


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
