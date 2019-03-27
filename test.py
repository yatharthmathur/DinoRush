import pygame
from OpenGL import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def init():
    gluOrtho2D(0,800,0,600)
    glClearColor(1,1,1,0)


def loadTexture():
    textureSurface = pygame.image.load('assets/background.jpg')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid

def background():
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(0, 0,0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(800, 0,0)
    glTexCoord2f(1.0, 1.0,)
    glVertex3f(800,  600,0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(0,  600,0)
    glEnd()
    glFlush()


pygame.init()
pygame.display.set_caption("DinoRush")
screen = pygame.display.set_mode((800,600), OPENGLBLIT|DOUBLEBUF|OPENGL)
init()
loadTexture()
clock = pygame.time.Clock()
x1,y1 = (100,100)
x2,y2 = (200,300)
x3,y3 = (400,100)
while True:
    background()
    clock.tick(60)

    glBegin(GL_POLYGON)
    glVertex(x1,y1)
    glVertex(x2,y2)
    glVertex(x3,y3)
    glEnd()
    x1+=1
    x2+=1
    x3+=1

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.flip()
pygame.quit()
quit()
