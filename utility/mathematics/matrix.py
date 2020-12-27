import os
import sys
import pygame as pg

import math

sys.path.insert(1,os.getcwd())

from utility.str_to_float import stf

class Matrix:
    def __init__(self, collums):
        l = len(collums[0])
        for x in collums:
            if len(x) != l:
                raise Exception('All collums need to have same size')

        self.data = collums

    def transpose(self):
        res = []
        for x in range(len(self.data[0])):
            temp = []
            for y in range(len(self.data)):
                temp.append(self.data[y][x])
            res.append(temp)
        self.data = res

    def __repr__(self):
        for x in range(len(self.data[0])):
            for y in range(len(self.data)):
                print('{} '.format(self.data[y][x]), end='')
            print('')
        return ''

    def __add__(self, other):
        # if len(self.data) != len(other.data) or len(self.data[1]) != len(other.data[1]):
        #     raise Exception('Different matrix size')

        res = []
        for x in range(len(self.data)):
            tmp = []
            for y in range(len(self.data[0])):
                tmp.append(self.data[x][y] + other.data[x][y])
            res.append(tmp)

        return Matrix(res)

    def __mul__(self, other):

        if type(other) == type(self):
            if len(self.data) != len(other.data[0]):
                raise Exception('Matrix A has to have same number of collums as matrix B has rows')
            res = []
            for x in range(len(self.data)):
                tmp = []
                for y in range(len(self.data[0])):
                    val = 0
                    for z in range(len(self.data)):
                        val += self.data[z][y]*other.data[x][z]
                    tmp.append(val)
                res.append(tmp)
            return Matrix(res)

        elif type(other) in (int, float):
            res = []
            for x in range(len(self.data)):
                tmp = []
                for y in range(len(self.data[0])):
                    tmp.append(self.data[x][y]*other)
                res.append(tmp)
            return Matrix(res)

    def rotate(self,ammount,offset=[0,0]):
        amt = math.radians(ammount)
        temp = [self.data[0][0]-offset[0],self.data[0][1]-offset[1]]
        temp = [math.cos(amt)*temp[0]+math.sin(amt)*temp[1],-math.sin(amt)*temp[0]+math.cos(amt)*temp[1]]
        self.data[0] = [temp[0]+offset[0],temp[1]+offset[1]]

    def mtl(self):
        temp = []
        for x in self.data[0]:
            temp.append(stf(x))
        return temp

    def magnitude(self):
        return math.sqrt(self.data[0][0]**2+self.data[0][1]**2)

    def normalize(self):
        return Matrix([[self.data[0][0]/self.magnitude(),self.data[0][1]/self.magnitude()]])
