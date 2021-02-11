import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.str_to_float import stf

from utility.mathematics.matrix import Matrix

class gravity:
    def __init__(self):
        self.type = 'gravity'
        self.attributes = {'force':Matrix([['0','-9.81']]),
        'test':Matrix([['1','1','1']])}

    def apply(self,particles,framerate):
        for x in particles.particles:
            x.velocity.data[0][0] -= stf(self.attributes['force'].data[0][0])/framerate
            x.velocity.data[0][1] -= stf(self.attributes['force'].data[0][1])/framerate
