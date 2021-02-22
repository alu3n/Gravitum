import os
import sys
import pygame as pg

"""
This file takes care of particle source visualisation.
Based on user specified parameters the function renders graphics on screen
that should help user to better imagine how would his simulation look like.
"""

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix

def source_viz(pos,camera,screen,size,rotate,spread):

    center = [camera.x+pos[0]*camera.scale,camera.y+pos[1]*camera.scale]
    pg.draw.circle(screen,[0,0,0],center,1*camera.scale*size)
    pg.draw.circle(screen,[30,60,30],[camera.x+pos[0]*camera.scale,camera.y+pos[1]*camera.scale],1*camera.scale*size-2)

    pointer = Matrix([[center[0],center[1]-camera.scale*size]])
    pointer.rotate(rotate,center)

    l0 = Matrix([[pointer.data[0][0],pointer.data[0][1]]])
    l1 = Matrix([[pointer.data[0][0],pointer.data[0][1]]])
    l2 = Matrix([[pointer.data[0][0],pointer.data[0][1]]])

    l0.rotate(spread/2,center)
    l1.rotate(-spread/2,center)


    pg.draw.line(screen, [0,0,0], center, [l0.data[0][0],l0.data[0][1]],2)
    pg.draw.line(screen, [0,0,0], center, [l1.data[0][0],l1.data[0][1]],2)
    pg.draw.line(screen, [25,25,25], center, [l2.data[0][0],l2.data[0][1]],2)


    pg.init()
    font = pg.font.Font('freesansbold.ttf', int(camera.scale*1.5))

    text = font.render('Source', True, [255,255,255])
    textRect = text.get_rect(center=(center[0],center[1]))
    screen.blit(text, textRect)
    # print('x')
