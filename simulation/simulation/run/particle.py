import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix

class particle:
    def __init__(self,position,velocity,color_start,color_end,lifespan,size,size_end):
        self.position = position
        self.velocity = velocity
        self.color = color_start
        self.color_end = color_end
        self.lifespan = lifespan
        self.size = size
        self.size_end = size_end

    def update(self,framerate):
        self.position = Matrix([[
        self.position.data[0][0]+self.velocity.data[0][0]/framerate,
        self.position.data[0][1]+self.velocity.data[0][1]/framerate
        ]])

        self.lifespan.data[0][0] -= 1

        self.color = Matrix([[
        self.color.data[0][0] + (self.color_end.data[0][0]-self.color.data[0][0])/self.lifespan.data[0][0],
        self.color.data[0][1] + (self.color_end.data[0][1]-self.color.data[0][1])/self.lifespan.data[0][0],
        self.color.data[0][2] + (self.color_end.data[0][2]-self.color.data[0][2])/self.lifespan.data[0][0]
        ]])

        self.size = Matrix([[
        self.size.data[0][0] + (self.size_end.data[0][0]-self.size.data[0][0])/self.lifespan.data[0][0],
        ]])
