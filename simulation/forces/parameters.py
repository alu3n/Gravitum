import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())


from utility.mathematics.matrix import Matrix



#Main simulation parameters
#Frames = count of simulated frames


class parameters:
    def __init__(self):
        self.type = 'parameters'
        self.attributes = {'framerate':Matrix([['24']]),
        'frames':Matrix([['240']]),
        'export resolution':Matrix([['1920','1080']]),
        'export background color':Matrix([['0','0','0']])
        }
