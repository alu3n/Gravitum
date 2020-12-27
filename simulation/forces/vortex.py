import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())


from utility.mathematics.matrix import Matrix

class vortex:
    def __init__(self):
        self.type = 'vortex'
        self.attributes = {'position':Matrix([['0','0']]),
        'speed':Matrix([['1']]),
        'range':Matrix([['10']])}
