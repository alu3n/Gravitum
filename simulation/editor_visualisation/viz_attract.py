import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix

def attract_viz(pos,camera,screen,size):

    center = [camera.x+pos[0]*camera.scale,camera.y+pos[1]*camera.scale]
    pg.draw.circle(screen,[0,0,0],center,1*camera.scale*size)
    pg.draw.circle(screen,[30,60,30],[camera.x+pos[0]*camera.scale,camera.y+pos[1]*camera.scale],1*camera.scale*size-2)


    pg.init()
    font = pg.font.Font('freesansbold.ttf', int(camera.scale*1.5))

    text = font.render('Attract', True, [255,255,255])
    textRect = text.get_rect(center=(center[0],center[1]))
    screen.blit(text, textRect)
    # print('x')
