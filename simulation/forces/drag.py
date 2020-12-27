import os
import sys
import pygame as pg
import math

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix
from utility.str_to_float import stf

class drag:
    def __init__(self):
        self.type = 'drag'
        self.attributes = {'multiplier':Matrix([['1']])}

    def apply(self,particles,framerate):
        for x in range(len(particles.particles)):
            multiplier = stf(self.attributes['multiplier'].data[0][0])
            magnitude = particles.particles[x].velocity.magnitude()
            area  = ((particles.particles[x].size.data[0][0]/2*math.pi)**2)
            unit_vector = particles.particles[x].velocity.normalize()
            drag = Matrix([[
                magnitude*multiplier*unit_vector.data[0][0]*(-1)/framerate,
                magnitude*multiplier*unit_vector.data[0][1]*(-1)/framerate
            ]])
            particles.particles[x].velocity = particles.particles[x].velocity + drag
            # particles.particles[x].velocity.data[0][0] += drag.data[0][0]
            # particles.particles[x].velocity.data[0][1] += drag.data[0][1]
