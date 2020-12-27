import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix
from scenes.editor import editor


from scenes.editor import editor
from scenes.export import export
from scenes.playback import playback


class display:
    def __init__(self,size,framerate,title,scene,minsize=Matrix([[600,400]])):
        if type(size) != Matrix:
            raise Exception('Size must be 2 by 1 matrix')
        elif len(size.data) != 1 or len(size.data[0]) != 2:
            raise Exception('Size must be 2 by 1 matrix')
        if type(framerate) != (int):
            raise Exception('Framerate must be int value 1 <= framerate <= 120')
        elif framerate > 120 or framerate < 1:
            raise Exception('Framerate must be int value 1 <= framerate <= 120')

        self.scene = scene

        self.framerate = framerate
        self.size = size
        self.screen = pg.display.set_mode(self.size.data[0],pg.RESIZABLE)
        self.clock = pg.time.Clock()
        self.minsize = minsize
        pg.init()
        pg.display.set_caption(title)

    def change_scene(self,scene):
        # if type(scene) != Scene:
        #     raise Exception('Scene must be scene type')
        self.scene = scene

    def update(self,event,data):
        if pg.display.get_surface().get_size()[0] < self.minsize.data[0][0]:
            pg.display.set_mode([self.minsize.data[0][0],pg.display.get_surface().get_size()[1]],pg.RESIZABLE)
        if pg.display.get_surface().get_size()[1] < self.minsize.data[0][1]:
            pg.display.set_mode([pg.display.get_surface().get_size()[0],self.minsize.data[0][1]],pg.RESIZABLE)

        status = self.scene.run(event,self.screen,data)
        if status != None:
            # print('x')
            return status

        pg.display.flip()
        self.clock.tick(self.framerate)

    def run(self,data):
        while True:
            status = None
            ev = None
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    return
                status = self.update(event,data)
            if status != None:
                return status
            else:
                self.update(None,data)
