import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.gui.elements.display_frame import display_frame

from utility.mathematics.matrix import Matrix
from template.scene import scene
from simulation.camera import camera
from playback.player import player
from utility.io.load import load
from playback.player import player

"""
This file takes care of image export
"""

class export:
    def __init__(self):
        self.loaded = False

    def load(self):
        self.data = load()
        self.loaded = True
        self.player = player(self.data.particles)


    def export(self,screen,size,color,camera_):

        """
        this method creates new screen that is not displayed, its just
        used to export user specified resolution
        """

        scr = screen
        screen = pg.Surface(size)

        cam = camera()

        m0 = size[0]/screen.get_size()[0]
        m1 = size[1]/screen.get_size()[1]
        mult = m0*m1
        cam.scale = camera_.scale
        cam.scale *= mult

        cam.offsetx = camera_.offsetx
        cam.offsety = camera_.offsety


        screen.fill(color)

        #Go through all frames and export each one

        for x in range(0,len(self.player.data)):
            display_frame(scr,'{}/{}'.format(x,len(self.player.data)),'Exporting')
            screen.fill(color)
            cam.update_export(screen, None)
            self.player.next(screen,cam,True)
            pg.image.save(screen, 'images/export{}.png'.format(x))
