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

class export:
    def __init__(self):
        self.loaded = False

    def load(self):
        self.data = load()
        self.loaded = True
        self.player = player(self.data.particles)


    def export(self,screen,size,color,camera_):

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

        for x in range(0,len(self.player.data)):
            display_frame(scr,'{}/{}'.format(x,len(self.player.data)),'Exporting')
            screen.fill(color)
            cam.update_export(screen, None)
            self.player.next(screen,cam)
            pg.image.save(screen, 'images/export{}.png'.format(x))
