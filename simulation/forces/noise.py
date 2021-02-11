import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())
import random


from utility.mathematics.matrix import Matrix
from utility.str_to_float import stf

class noise_vector:
    def __init__(self,pos):
        self.pos = Matrix([pos])
        self.direction = Matrix([[2*(.5-random.random()),2*(.5-random.random())]])

class noise:
    def __init__(self):
        self.type = 'noise'
        self.attributes = {'separation':Matrix([['5']]),
        'multiplier':Matrix([['1']]),
        'range':Matrix([['30']])}
        self.active = False

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

    def apply(self,particles,framerate):
        self.fld()
        rng = stf(self.attributes['range'].data[0][0])
        mult = stf(self.attributes['multiplier'].data[0][0])
        # print(self.field_dict)
        for x in particles.particles:
            p_x = int(x.position.data[0][0]//rng)
            p_y = int(x.position.data[0][1]//rng)
            adress = '{}:{}'.format(p_x,p_y)
            # print(adress)
            if adress in self.field_dict.keys():
                # print('test')
                x.velocity.data[0][0] += self.field_dict[adress].pos.data[0][0]/framerate*mult
                x.velocity.data[0][1] += self.field_dict[adress].pos.data[0][1]/framerate*mult
