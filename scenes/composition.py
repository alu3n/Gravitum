import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix


from template.display import display

from scenes.editor import editor
from scenes.export import export
from scenes.playback import playback
from scenes.startup_solvers import data

from utility.str_to_float import stf

"""
Main scene class
this class is for switching between scenes (editor, export and playback)
"""

class composition:
    def __init__(self):
        # self.data = data
        self.data = data()

        self.export = export()
        self.playback = playback()

        self.display = display(Matrix([[960,600]]),60,'Gravitum',self.playback)
        self.editor = editor(self.data,self.display.screen)
        self.display.change_scene(self.editor)

    def run(self):
        while True:
            status = self.display.run(self.data)
            if status == 'editor':
                self.framerate = 60
                self.display.change_scene(self.editor)
            elif status == 'export':
                fr = int(stf(self.data.solvers[0].attributes['framerate'].data[0][0]))
                if fr < 1:
                    self.framerate = 60
                else:
                    self.framerate = 1000
                if self.export.loaded:
                    self.display.change_scene(self.export)
            elif status == 'playback':
                fr = int(stf(self.data.solvers[0].attributes['framerate'].data[0][0]))
                if fr < 1:
                    self.framerate = 1000
                else:
                    self.framerate = fr
                self.display.change_scene(self.playback)
            elif status == 'playbackload':
                fr = int(stf(self.data.solvers[0].attributes['framerate'].data[0][0]))
                if fr < 1:
                    self.framerate = 60
                else:
                    self.framerate = 1000
                self.playback.load()
                self.export.load()
                self.display.change_scene(self.playback)
            else:
                return

c = composition()
c.run()
