import os
import sys
import pygame as pg
import json

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix

"""
Class that is made to save cache to memory
"""

class save:
    def __init__(self):
        self.frames = {}

    def load_frame(self,particles,frame):
        temp = []
        for x in particles.particles:
            temp.append([
            x.position.data[0],
            x.color.data[0],
            x.size.data[0][0]
            ])
        self.frames[str(frame)] = temp

    def save(self):
        with open('cache/cache.json', 'w+') as json_file:
            json.dump(self.frames, json_file)
