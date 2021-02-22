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

"""
Solvers that will be created when user starts the software
"""

class data:
    def __init__(self):
        self.solvers = [parameters(),source(),gravity()]
