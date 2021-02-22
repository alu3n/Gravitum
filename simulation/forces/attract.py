import os
import sys
import pygame as pg
import math

"""
Solver that is emulating magnet force.
Attributes:
- Position - Where in space does it affect simulation
- Multiplier - Force multiplier
- Range - How far does the force reach from the center of its possition
"""


sys.path.insert(1,os.getcwd())

from utility.str_to_float import stf
from utility.mathematics.matrix import Matrix



class attract:
    def __init__(self):
        self.type = 'attract'

        #Attract force attributes

        self.attributes = {'position':Matrix([['0','0']]),
        'multiplier':Matrix([['1']]),
        'range':Matrix([['10']])}

    def apply(self,particles,framerate):
        #Load values from attributes specified by the user
        center = self.attributes['position'].data[0]
        range_ = self.attributes['range'].data[0][0]
        multiplier = self.attributes['multiplier'].data[0][0]

        #Loop through all particles - apply attract force to each one

        for x in range(len(particles.particles)):

            #Compute distance from the center of the attract solver to the particle

            distance = math.sqrt(
            abs((stf(center[0])-particles.particles[x].position.data[0][0])**2+
            (stf(center[1])-particles.particles[x].position.data[0][1])**2))

            #If is the particle in range of the solver...apply the force

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
