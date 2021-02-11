import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix

from utility.str_to_float import stf

from simulation.forces.gravity import gravity
from simulation.forces.drag import drag
from simulation.forces.source import source
from simulation.forces.noise import noise
from simulation.forces.attract import attract
from simulation.forces.vortex import vortex
from simulation.forces.parameters import parameters

def move_forces(event,data,selected):
    if event != None and selected != None:
        if event.type == pg.KEYDOWN:
            if type(data.solvers[selected]) in [type(source()),type(attract()),type(vortex())]:
                if event.key == pg.K_LEFT:
                    data.solvers[selected].attributes['position'].data[0][0] = str(stf(data.solvers[selected].attributes['position'].data[0][0])-2.5)
                if event.key == pg.K_RIGHT:
                    data.solvers[selected].attributes['position'].data[0][0] = str(stf(data.solvers[selected].attributes['position'].data[0][0])+2.5)
                if event.key == pg.K_UP:
                    data.solvers[selected].attributes['position'].data[0][1] = str(stf(data.solvers[selected].attributes['position'].data[0][1])+2.5)
                if event.key == pg.K_DOWN:
                    data.solvers[selected].attributes['position'].data[0][1] = str(stf(data.solvers[selected].attributes['position'].data[0][1])-2.5)
