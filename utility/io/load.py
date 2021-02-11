import os
import sys
import pygame as pg
import json

sys.path.insert(1,os.getcwd())

class load:
    def __init__(self):
        with open('cache/cache.json', 'r') as read_file:
            data = json.load(read_file)
        rtv = []
        for x in data:
            rtv.append(data[x])
        self.particles = rtv
