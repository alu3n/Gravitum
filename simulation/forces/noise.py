import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())
import random


from utility.mathematics.matrix import Matrix
from utility.str_to_float import stf

"""
Solver that is emulating wind force.
- Noise solver creates field of individual noise vectors, particles
 are affected by the closest one to them.
Attributes:
- separation - distance between individual noise vectors in the field
- multiplier - how much does the vectors affect particles
- range - range = x => there is x*x vectors
"""


#Noise vector pointing to random direction
class noise_vector:
    def __init__(self,pos):
        self.pos = Matrix([pos])
        self.direction = Matrix([[2*(.5-random.random()),2*(.5-random.random())]])

#Noise field function
class noise:
    def __init__(self):
        self.type = 'noise'

        #Attributes for user to specify

        self.attributes = {'separation':Matrix([['5']]),
        'multiplier':Matrix([['1']]),
        'range':Matrix([['30']])}
        self.active = False

    #Noise field - create field of noise vectors
    def fld(self):
        self.active = True
        self.field = []
        if stf(self.attributes['range'].data[0][0]) >= 100:
            rng = 100
        else:
            rng = stf(self.attributes['range'].data[0][0])
        if stf(self.attributes['separation'].data[0][0]) <= 1:
            sep = 1
        else:
            sep = stf(self.attributes['separation'].data[0][0])

        self.field_dict = {}
        for x in range(1+int(rng)):
            for y in range(1+int(rng)):
                nv = noise_vector([x*sep-sep*rng/2,y*sep-sep*rng/2])
                adress = '{}:{}'.format(int(rng/2)-x,int(rng/2)-y)
                self.field.append(nv)
                self.field_dict[adress] = nv

    #Apply noise field to particles
    def apply(self,particles,framerate):
        self.fld()
        rng = stf(self.attributes['range'].data[0][0])
        mult = stf(self.attributes['multiplier'].data[0][0])

        #Loop through the particles

        for x in particles.particles:

            """
            If the particle is inside noise field adress range, apply the noise
            Noise is separated into chunks each noise vector has its adress
            Applied noise is the closest vector
            """

            p_x = int(x.position.data[0][0]//rng)
            p_y = int(x.position.data[0][1]//rng)
            adress = '{}:{}'.format(p_x,p_y)
            if adress in self.field_dict.keys():
                x.velocity.data[0][0] += self.field_dict[adress].pos.data[0][0]/framerate*mult
                x.velocity.data[0][1] += self.field_dict[adress].pos.data[0][1]/framerate*mult
