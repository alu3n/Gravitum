import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix
from simulation.camera import camera

from simulation.forces.source import source
from simulation.forces.noise import noise
from simulation.forces.vortex import vortex
from simulation.forces.attract import attract

from simulation.editor_visualisation.viz_source import source_viz
from simulation.editor_visualisation.viz_noise import viz_noise
from simulation.editor_visualisation.viz_vortex import viz_vortex
from simulation.editor_visualisation.viz_attract import attract_viz

from utility.gui.elements.editor_info import editor_info

from utility.str_to_float import stf

class visualise:
    def __init__(self):
        self.camera = camera()
        self.editor_info = editor_info()
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
            if type(x) == type(attract()):
                attract_viz([stf(x.attributes['position'].data[0][0]),
                -stf(x.attributes['position'].data[0][1])],
                self.camera,
                screen,stf(x.attributes['range'].data[0][0]))
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
        self.editor_info.update(screen,self.camera.scale,[self.camera.offsetx,self.camera.offsety])
        # self.camera.viz(screen)
