import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix
from utility.gui.button import button
from utility.gui.editor.solver_menu_add_remove import add_remove
from utility.gui.editor.solver_menu_add_popup import add_popup
from utility.gui.editor.solver_menu_solvers import menu_solvers
from utility.gui.editor.solver_menu_solver_properties import solver_properties
from utility.gui.elements.textbox_cluster import textbox_cluster

from utility.gui.elements.textbox import textbox

from simulation.forces.gravity import gravity
from simulation.forces.drag import drag
from simulation.forces.source import source
from simulation.forces.noise import noise
from simulation.forces.attract import attract
from simulation.forces.vortex import vortex
from simulation.forces.parameters import parameters

class solver_menu:
    def __init__(self,data,screen):
        self.width = 300
        self.add_remove_height = 30
        self.adding = False


        self.add_popup = add_popup()
        self.add_remove = add_remove(self.width,self.add_remove_height)
        self.menu_solvers = menu_solvers()

        self.textbox_cluster = textbox_cluster()

        self.selected = None

        self.solver_properties = solver_properties(data,self.selected,screen)


    def update_buttons(self,screen):
        pass

    def render(self,screen):
        pass

    def update(self,event,screen,data):
        self.run(event,screen,data)

    def run(self,event,screen,data):

        self.solver_properties.update(event,screen,data,selected=self.selected)

        val_solvers = self.menu_solvers.update(event,screen,data,self.selected)

        if val_solvers != None:
            self.selected = val_solvers
            self.textbox_cluster.load(data,self.selected)
            # print(data.solvers[val_solvers].attributes)

        self.textbox_cluster.update(screen,data,event)

        val = self.add_remove.update(event,screen)

        if val == 'add':
            self.adding = True
        elif val == 'remove':
            if self.selected != None:
                if type(data.solvers[self.selected]) != type(parameters()):
                    print(type(self.selected))
                    self.textbox_cluster.unload()
                    data.solvers.pop(self.selected)
                    self.selected = None

        if self.adding:
            val_popup = self.add_popup.update(event,screen)
            if val_popup != None:
                if val_popup == 'gravity':
                    data.solvers.append(gravity())
                elif val_popup == 'drag':
                    data.solvers.append(drag())
                elif val_popup == 'source':
                    data.solvers.append(source())
                elif val_popup == 'noise':
                    data.solvers.append(noise())
                elif val_popup == 'vortex':
                    data.solvers.append(vortex())
                elif val_popup == 'attract':
                    data.solvers.append(attract())
                self.adding = False
                # for x in data.solvers[1].attributes:
                #     print(data.solvers[1].attributes[x].data[0][0])
            # print(data.solvers[0].attributes['multiplier'].data[0][0])

        # self.test_txbx.update(screen,Matrix([[500,500]]),event)
