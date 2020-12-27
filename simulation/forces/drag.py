import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix

class drag:
    def __init__(self):
        self.type = 'drag'
        self.attributes = {'multiplier':Matrix([['1']])}
