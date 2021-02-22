import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.str_to_float import stf

from utility.mathematics.matrix import Matrix
from template.scene import scene
from simulation.camera import camera
from utility.gui.button import button
from export.export_player import player
from export.export_image import export as exp
from utility.io.load import load

"""
Export program window
"""

class export(scene):
    def __init__(self):
        super().__init__()
        self.cam = camera()
        self.export = exp()
        self.loaded = False
        self.button = button('export',Matrix([[150,50]]),Matrix([[100,30]]),'export',font_size=20)

    def load(self):
        self.data = load()
        self.loaded = True
        self.player = player(self.data.particles)

    def update_button(self,screen,event):
        self.button.position = Matrix([[screen.get_size()[0]/2,screen.get_size()[1]-50]])
        val = self.button.update(screen, event)
        return val


    def run(self,event,screen,data):
        color = data.solvers[0].attributes['export background color'].mtl()
        res_export = data.solvers[0].attributes['export resolution'].mtl()
        res_window = [screen.get_size()[0],screen.get_size()[1]-40]

        ex_aspect = res_export[0]/res_export[1]
        wi_aspect = res_window[0]/res_window[1]

        screen.fill([0,0,0])

        for x in range(len(color)):
            if color[x] > 255:
                color[x] = 255
            elif color[x] < 0:
                color[x] = 0


        if ex_aspect > wi_aspect:
            x = 0
            y = 20+(screen.get_size()[1]-(screen.get_size()[0]-40)/ex_aspect)/2
            s_x = screen.get_size()[0]
            s_y = (screen.get_size()[0]-40)/ex_aspect

            pg.draw.rect(screen,[255,0,0],(x,y,s_x,s_y))
            pg.draw.rect(screen,color,(x+2,y+2,s_x-4,s_y-4))
        else:
            x = (screen.get_size()[0]-screen.get_size()[1]*ex_aspect)/2
            y = 40
            s_x = screen.get_size()[1]*ex_aspect
            s_y = screen.get_size()[1]
            pg.draw.rect(screen,[255,0,0],(x,y,s_x,s_y))
            pg.draw.rect(screen,color,(x+2,y+2,s_x-4,s_y-44))

        self.cam.update_export(screen,event)

        if self.loaded:
            self.player.next(screen,self.cam,res_export)

        val = self.update_button(screen,event)
        if val == 'export':
            self.export.load()
            self.export.export(screen,res_export,color,self.cam)


        return(super().run(event,screen,data))
