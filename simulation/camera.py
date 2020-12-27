import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix

class camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.scale = 10
        self.offsetx = 0
        self.offsety = 0


    def update(self, screen, event):
        self.x = screen.get_size()[0]/2+self.offsetx
        self.y = screen.get_size()[1]/2+self.offsety
        if event != None:
            if event.type == pg.KEYDOWN:
                # print(event)
                if event.unicode == '':
                    pass
                elif event.unicode in 'q':
                    if self.scale != 1:
                        self.scale -= 1
                elif event.unicode in 'e':
                    self.scale += 1
                elif event.unicode in 's':
                    self.offsety += self.scale
                elif event.unicode in 'w':
                    self.offsety -= self.scale
                elif event.unicode in 'a':
                    self.offsetx -= self.scale
                elif event.unicode in 'd':
                    self.offsetx += self.scale
        self.viz(screen)

    def viz(self,screen):
        color_lines = [40,80,40]
        color_lead_lines = [40,90,40]
        for x in range(screen.get_size()[0]//int(self.scale*2.5)):
            pg.draw.line(screen,color_lines,[self.x+x*self.scale*2.5,0],[self.x+x*self.scale*2.5,screen.get_size()[1]])
            pg.draw.line(screen,color_lines,[self.x-x*self.scale*2.5,0],[self.x-x*self.scale*2.5,screen.get_size()[1]])
        for x in range(screen.get_size()[1]//int(self.scale*2.5)):
            pg.draw.line(screen,color_lines,[0,self.y+x*self.scale*2.5],[screen.get_size()[0],self.y+x*self.scale*2.5])
            pg.draw.line(screen,color_lines,[0,self.y-x*self.scale*2.5],[screen.get_size()[0],self.y-x*self.scale*2.5])
        pg.draw.line(screen,color_lead_lines,[0,self.y],[screen.get_size()[0],self.y],2)
        pg.draw.line(screen,color_lead_lines,[self.x,0],[self.x,screen.get_size()[1]],2)
