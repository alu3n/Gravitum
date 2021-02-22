import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix

"""
Class that holds all simulation particles
"""

class particles:
    def __init__(self):
        self.particles = []
