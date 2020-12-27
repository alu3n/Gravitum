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
        self.fld()

    def fld(self):
        self.field = []
        if stf(self.attributes['range'].data[0][0]) >= 100:
            rng = 100
        else:
            rng = stf(self.attributes['range'].data[0][0])
        if stf(self.attributes['separation'].data[0][0]) <= 1:
            sep = 1
        else:
            sep = stf(self.attributes['separation'].data[0][0])



        for x in range(1+int(rng)):
            for y in range(1+int(rng)):
                pass
                self.field.append(
                noise_vector([x*sep-sep*rng/2,
                y*sep-sep*rng/2]))
