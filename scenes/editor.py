import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix
from template.scene import scene
from simulation.editor_visualisation.visualise import visualise
from utility.gui.editor.solver_menu import solver_menu
from simulation.simulation.load import load
from simulation.simulation.run.sim_runner import sim_runner

# from simulation.run import sim_runner import sim_runner

class editor(scene):
    def __init__(self,data,screen):
        super().__init__()
        self.visualise = visualise()
        self.solver_menu = solver_menu(data,screen)
        self.load = load()


        self.runner = sim_runner()

    def run(self,event,screen,data):
        screen.fill([30,60,30])
        self.visualise.update(data,screen,event)
        self.solver_menu.update(event,screen,data)


        val = self.load.update(screen,event)
        if val != None:
            self.runner.run(data,screen)
            return 'playbackload'

        return(super().run(event,screen,data))
