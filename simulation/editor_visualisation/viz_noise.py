import os
import sys
import pygame as pg

"""
This file takes care of noise visualisation.
Based on user specified parameters the function renders graphics on screen
that should help user to better imagine how would his simulation look like.
"""

sys.path.insert(1,os.getcwd())

from utility.str_to_float import stf
from utility.mathematics.matrix import Matrix


def viz_noise(screen, noise, camera):
    if noise.active:
        for x in noise.field:
            center = [camera.x+x.pos.data[0][0]*camera.scale,camera.y-x.pos.data[0][1]*camera.scale]
            pointer = [center[0]+x.direction.data[0][0]*camera.scale*stf(noise.attributes['multiplier'].data[0][0]),center[1]+x.direction.data[0][1]*camera.scale*stf(noise.attributes['multiplier'].data[0][0])]
            pg.draw.line(screen, [222,99,99], center, pointer,1)
