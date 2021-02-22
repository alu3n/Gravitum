import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix

"""
This class is made to represent single particle and its attributes
Its method update changes particle attributes based on its properties
"""

class particle:
    def __init__(self,position,velocity,color_start,color_end,lifespan,size,size_end):

        #Particle attributes for the simulation

        """
        position: ...
        velocity: force with direction
        color: color at this exact moment
        color_end: color that will the particle reach when it has no lifetime left
        lifespan: how many frames does the particle have until dead
        size: size of the particle at this moment
        size_end: size that will the particle reach when it has no lifetime left
        """

        self.position = position
        self.velocity = velocity
        self.color = color_start
        self.color_end = color_end
        self.lifespan = lifespan
        self.size = size
        self.size_end = size_end

    def update(self,framerate):

        #Update particle possition, color and size based on particle parameters

        self.position = Matrix([[
        self.position.data[0][0]+self.velocity.data[0][0]/framerate,
        self.position.data[0][1]+self.velocity.data[0][1]/framerate
        ]])

        self.color = Matrix([[
        self.color.data[0][0] + (self.color_end.data[0][0]-self.color.data[0][0])/self.lifespan.data[0][0],
        self.color.data[0][1] + (self.color_end.data[0][1]-self.color.data[0][1])/self.lifespan.data[0][0],
        self.color.data[0][2] + (self.color_end.data[0][2]-self.color.data[0][2])/self.lifespan.data[0][0]
        ]])

        self.size = Matrix([[
        self.size.data[0][0] + (self.size_end.data[0][0]-self.size.data[0][0])/self.lifespan.data[0][0],
        ]])

        self.lifespan.data[0][0] -= 1
