import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())


from utility.mathematics.matrix import Matrix

import random

from simulation.simulation.run.particle import particle

from utility.str_to_float import stf

class source:
    def __init__(self):
        self.type = 'source'
        self.attributes = {'position':Matrix([['0','0']]),
        'frequency':Matrix([['1']]),
        'direction':Matrix([['0']]),
        'spread':Matrix([['0']]),
        'range':Matrix([['5']]),
        'color min start':Matrix([['0','0','0']]),
        'color max start':Matrix([['255','255','255']]),
        'color min end':Matrix([['0','0','0']]),
        'color max end':Matrix([['255','255','255']]),
        'velocity':Matrix([['0','100']]),
        'lifespan':Matrix([['0','100']]),
        'size start':Matrix([['0','1']]),
        'size end':Matrix([['0','1']])
        }
        self.tick = 1

    def source(self,particles):
        position = self.attributes['position'].mtl()
        direction = self.attributes['direction'].mtl()
        spread = self.attributes['spread'].mtl()
        range_a = self.attributes['range'].mtl()
        color_min = self.attributes['color min start'].mtl()
        color_max = self.attributes['color max start'].mtl()
        color_min_end = self.attributes['color min end'].mtl()
        color_max_end = self.attributes['color max end'].mtl()
        velocity = self.attributes['velocity'].mtl()
        lifespan = self.attributes['lifespan'].mtl()
        size_start = self.attributes['size start'].mtl()
        size_end = self.attributes['size end'].mtl()

        frequency = int(stf(self.attributes['frequency'].data[0][0]))

        size = Matrix([[size_start[0]+(size_start[1]-size_start[0])*random.random()]])
        size_e = Matrix([[size_end[0]+(size_end[1]-size_end[0])*random.random()]])

        color_start = Matrix([[
        color_min[0]+(color_max[0]-color_min[0])*random.random(),
        color_min[1]+(color_max[1]-color_min[1])*random.random(),
        color_min[2]+(color_max[2]-color_min[2])*random.random()
        ]])

        for x in range(len(color_start.data[0])):
            temp = int(color_start.data[0][x])
            if temp > 255:
                temp = 255
            elif temp < 0:
                temp = 0
            color_start.data[0][x] = temp

        color_end = Matrix([[
        color_min_end[0]+(color_max_end[0]-color_min_end[0])*random.random(),
        color_min_end[1]+(color_max_end[1]-color_min_end[1])*random.random(),
        color_min_end[2]+(color_max_end[2]-color_min_end[2])*random.random()
        ]])

        for x in range(len(color_end.data[0])):
            temp = int(color_end.data[0][x])
            if temp > 255:
                temp = 255
            elif temp < 0:
                temp = 0
            color_end.data[0][x] = temp

        vel = Matrix([[0,1]])
        vel.data[0][1] = range_a[0]*vel.data[0][1] + (velocity[1]-velocity[0])*random.random()
        vel.rotate(direction[0]-180)
        vel.rotate(spread[0]/2-random.random()*spread[0])

        lfsp = Matrix([[int(lifespan[0]+(lifespan[1]-lifespan[0])*random.random())]])


        if frequency < 1:
            frequency = 1

        if self.tick == frequency:
        # for t in range(20):
            particles.particles.append(particle(Matrix([[position[0],-position[1]]]),vel,color_start,color_end,lfsp,size,size_e))
            self.tick = 0
            # for x in particles.particles:
            #     print(x)
            #     print(x.size.data[0])
            #     print(x.size_end.data[0])



        self.tick += 1
