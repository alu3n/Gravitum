import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())


from utility.mathematics.matrix import Matrix

class parameters:
    def __init__(self):
        self.type = 'parameters'
        self.attributes = {'framerate':Matrix([['24']]),
        'frames':Matrix([['120']])
        }
