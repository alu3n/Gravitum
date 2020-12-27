import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix

from simulation.forces.gravity import gravity
from simulation.forces.drag import drag
from simulation.forces.source import source
from simulation.forces.noise import noise
from simulation.forces.vortex import vortex
from simulation.forces.parameters import parameters


class data:
    def __init__(self):
        self.solvers = [parameters(),source(),gravity()]

    def add_solver(self):
        pass

    def remove_solver(self):
        pass
