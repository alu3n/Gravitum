import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

"""
This function is made to prevent problems with values that could output error
"""

def stf(text):
    if len(text) == 0:
        return 0.0
    if text == '-':
        return -0.0
    if text == '-.':
        return -.0
    if text == '.':
        return .0
    else:
        return float(text)
