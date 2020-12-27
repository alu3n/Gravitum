import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix
from simulation.simulation.run.particle import particle
from simulation.simulation.run.particles import particles

from utility.str_to_float import stf

from simulation.forces.gravity import gravity
from simulation.forces.drag import drag
from simulation.forces.source import source
from simulation.forces.noise import noise
from simulation.forces.vortex import vortex
from simulation.forces.attract import attract
from simulation.forces.parameters import parameters

from utility.io.save import save


class sim_runner:
    def __init__(self):
        self.particles = particles()
        self.save = save()

    def run(self,data):
        self.data = data

        self.framerate = int(stf(self.data.solvers[0].attributes['framerate'].data[0][0]))
        self.frames = self.data.solvers[0].attributes['frames'].data[0][0]

        self.particles.particles = []

        for y in range(int(stf(self.frames))):
            for x in self.data.solvers:
                if type(x) == type(source()):
                    x.source(self.particles)
                if type(x) == type(gravity()):
                    x.apply(self.particles,self.framerate)
                if type(x) == type(drag()):
                    x.apply(self.particles,self.framerate)
                if type(x) == type(vortex()):
                    x.apply(self.particles,self.framerate)
                if type(x) == type(attract()):
                    x.apply(self.particles,self.framerate)
            new = []
            for x in range(len(self.particles.particles)):
                if self.particles.particles[x].lifespan.data[0][0] > 1:
                    self.particles.particles[x].update(self.framerate)
                    new.append(self.particles.particles[x])
            self.particles.particles = new

            self.save.load_frame(self.particles,y)
        self.save.save()
