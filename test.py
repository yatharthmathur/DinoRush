import pygame
from OpenGL import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
def init():
    gluOrtho2D(0,800,0,600)
    glClearColor(0,0,0,1)
    glClearDepth(1)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA)



def draw_text(text, x, y):
    glRasterPos3f(x,y,1)
    for x in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(x))
    glFlush()


pygame.init()
pygame.display.set_caption("DinoRush")
screen = pygame.display.set_mode((800,600), OPENGLBLIT|DOUBLEBUF|OPENGL)
glutInit()
init()
draw_text("ABCD",400,300)
pygame.display.flip()
