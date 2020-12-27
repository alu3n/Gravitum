import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix

from simulation.forces.noise import noise

class textbox:
    def __init__(self,width,height,data_pointer,parameter,index,border=4):
        pg.init()
        self.width = width
        self.height = height
        self.border = border

        self.parameter = parameter
        self.index = index

        self.fresh = False

        self.selected = False
        self.data_pointer = data_pointer
        self.hover = False

        self.font = pg.font.Font('freesansbold.ttf', 12)

        self.rtrval = None

    def update_box(self, screen,position):
        self.display_text = self.font.render(self.data_pointer.attributes[self.parameter].data[0][self.index], True, [255,255,255])
        self.textRect = self.display_text.get_rect(center=(position.data[0][0],position.data[0][1]))
        self.rect = pg.Rect(position.data[0][0]-self.width/2,position.data[0][1]-self.height/2,self.width,self.height)

    def render(self,screen,position):
        if self.selected:
            color = [44,44,44]
        else:
            color = [120,120,120]

        pg.draw.rect(screen,[100,100,100],self.rect)
        pg.draw.rect(screen,color,(position.data[0][0]-self.width/2+self.border/2,position.data[0][1]-self.height/2+self.border/2,self.width-self.border,self.height-self.border))
        screen.blit(self.display_text, self.textRect)

    def detect_keys(self,event):
        if self.selected:
            if event != None:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.selected = False
                    if event.key == pg.K_BACKSPACE:
                        self.data_pointer.attributes[self.parameter].data[0][0] =  self.data_pointer.attributes[self.parameter].data[0][self.index][:-1]
                    else:
                        if self.fresh:
                            if event.unicode in '-0123456789.':
                                self.data_pointer.attributes[self.parameter].data[0][self.index] = event.unicode
                                # print(self.data_pointer.attributes[self.parameter].data[0][self.index])
                            self.fresh = False
                            if type(self.data_pointer) == type(noise()):
                                self.data_pointer.fld()
                        elif len(self.data_pointer.attributes[self.parameter].data[0][self.index]) == 0:
                            if event.unicode in '-0123456789.':
                                self.data_pointer.attributes[self.parameter].data[0][self.index] = event.unicode
                                print(self.data_pointer.attributes[self.parameter].data[0][self.index])
                            if type(self.data_pointer) == type(noise()):
                                self.data_pointer.fld()
                        else:
                            if event.unicode != '.' or event.unicode not in self.data_pointer.attributes[self.parameter].data[0][self.index]:
                                if event.unicode in '0123456789.':
                                    self.data_pointer.attributes[self.parameter].data[0][self.index] += event.unicode
                            if type(self.data_pointer) == type(noise()):
                                self.data_pointer.fld()


    def detect_selection(self,event):
        if event != None:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                if active:
                    self.selected = not self.selected
                    self.fresh = True
                    self.rtrval = True

    def update(self,screen,position,event):
        self.update_box(screen,position)
        self.detect_selection(event)
        self.detect_keys(event)
        self.render(screen,position)

        if self.rtrval != None:
            self.rtrval = None
            # print('x')
            return self
