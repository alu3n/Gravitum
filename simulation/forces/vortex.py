import os
import sys
import pygame as pg

import math

sys.path.insert(1,os.getcwd())

from utility.str_to_float import stf
from utility.mathematics.matrix import Matrix

"""
Solver that is emulating rotation force.
Attributes:
- Position - Where in space does it affect simulation
- Speed - Force multiplier
- Range - How far does the force reach from the center of its possition
"""

class vortex:
    def __init__(self):
        self.type = 'vortex'

        #Attributes for the user to specify

        self.attributes = {'position':Matrix([['0','0']]),
        'speed':Matrix([['1']]),
        'range':Matrix([['10']])}



    def apply(self,particles,framerate):
        center = self.attributes['position'].data[0]
        range_ = self.attributes['range'].data[0][0]
        speed = self.attributes['speed'].data[0][0]

        #Loop through all particles

        for x in range(len(particles.particles)):
            distance = math.sqrt(
            (stf(center[0])-particles.particles[x].position.data[0][0])**2+
            (stf(center[1])-particles.particles[x].position.data[0][1])**2
            )

            #If the particle is in range => apply force
            if distance < stf(range_):
                reference = Matrix([particles.particles[x].position.data[0]])
                reference.rotate(36,[stf(center[0]),stf(center[1])])
                vortex = Matrix([[
                (reference.data[0][0] + stf(center[0]))/framerate*stf(speed),
                (reference.data[0][1] + stf(center[0]))/framerate*stf(speed)
                ]])
                particles.particles[x].velocity += vortex
