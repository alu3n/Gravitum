import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

"""
You should run project using this file
"""

from scenes.composition import composition

c = composition()
c.run()
