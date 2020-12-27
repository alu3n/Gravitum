import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())


from scenes.composition import composition


c = composition()
c.run()
