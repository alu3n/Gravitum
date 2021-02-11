import os
import sys
import pygame as pg

import math

sys.path.insert(1,os.getcwd())

from utility.str_to_float import stf
from utility.mathematics.matrix import Matrix

class attract:
    def __init__(self):
        self.type = 'attract'
        self.attributes = {'position':Matrix([['0','0']]),
        'multiplier':Matrix([['1']]),
        'range':Matrix([['10']])}

    def apply(self,particles,framerate):
        center = self.attributes['position'].data[0]
        range_ = self.attributes['range'].data[0][0]
        multiplier = self.attributes['multiplier'].data[0][0]
        for x in range(len(particles.particles)):
            # print(x)
            distance = math.sqrt(
            abs((stf(center[0])-particles.particles[x].position.data[0][0])**2+
            (stf(center[1])-particles.particles[x].position.data[0][1])**2)
            )
            if distance < stf(range_):
                reference = Matrix([particles.particles[x].position.data[0]])
                attr = Matrix([[
                (reference.data[0][0] + stf(center[0])),
                (reference.data[0][1] + stf(center[0]))
                ]])
                if attr.data[0][0] != 0 or attr.data[0][1] != 0:
                    attr.normalize()
                    attr.data[0][0] *= 1/framerate*stf(multiplier)*(-1)
                    attr.data[0][1] *= 1/framerate*stf(multiplier)*(-1)
                    particles.particles[x].velocity += attr
