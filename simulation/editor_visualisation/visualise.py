import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix
from simulation.camera import camera

from simulation.forces.source import source
from simulation.forces.noise import noise
from simulation.forces.vortex import vortex

from simulation.editor_visualisation.viz_source import source_viz
from simulation.editor_visualisation.viz_noise import viz_noise
from simulation.editor_visualisation.viz_vortex import viz_vortex


from utility.str_to_float import stf

class visualise:
    def __init__(self):
        self.camera = camera()

    def update(self,data,screen,event):
        self.camera.update(screen, event)
        for x in data.solvers:
            if type(x) == type(noise()):
                viz_noise(screen,x,self.camera)
            if type(x) == type(vortex()):
                viz_vortex([stf(x.attributes['position'].data[0][0]),
                -stf(x.attributes['position'].data[0][1])],
                self.camera,
                screen,
                stf(x.attributes['range'].data[0][0]),
                stf(x.attributes['speed'].data[0][0])
                )
        for x in data.solvers:
            # print(type(x))
            if type(x) == type(source()):
                # print('x')
                source_viz([stf(x.attributes['position'].data[0][0]),
                -stf(x.attributes['position'].data[0][1])],
                self.camera,
                screen,stf(x.attributes['range'].data[0][0]),
                stf(x.attributes['direction'].data[0][0]),
                stf(x.attributes['spread'].data[0][0]))
        # self.camera.viz(screen)
