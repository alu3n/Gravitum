import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.str_to_float import stf

from utility.mathematics.matrix import Matrix

"""
Solver that is emulating magnet force.
Attributes:
- Position - Where in space does it affect simulation
- Multiplier - Force multiplier
- Range - How far does the force reach from the center of its possition
"""

class gravity:
    def __init__(self):
        self.type = 'gravity'

        #Gravity attributes for user to change

        self.attributes = {'force':Matrix([['0','-9.81']]),
        'test':Matrix([['1','1','1']])}

    def apply(self,particles,framerate):

        #Loop through particles
        for x in particles.particles:

            #Add gravity force to each particle

            x.velocity.data[0][0] -= stf(self.attributes['force'].data[0][0])/framerate
            x.velocity.data[0][1] -= stf(self.attributes['force'].data[0][1])/framerate
