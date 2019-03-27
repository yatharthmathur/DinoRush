import pygame
from OpenGL import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import math
import time

def init():
    gluOrtho2D(0,800,0,600)
    glClearColor(0,0,0,1)
    glClearDepth(1)
    glutInitDisplayMode(GLUT_SINGLE_GLUT_RGBA)
    glutBlendFunc(GL_SRC_APLPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)
