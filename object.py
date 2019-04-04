import pygame
from OpenGL import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import math
import time
#game settings
DISPLAY=(800,600)
CACT_SIZE=(35,70)
CACT_SPEED=[-2.5,0]

BIRD_SIZE=(35,35)
BIRD_SPEED=[-2.5,0]

PLAYER_SIZE=(35,70)
g = 0.08
textures=[0,0,0,0,0,0]
string = "GAME OVER"
#window properties


def init():
    gluOrtho2D(0,800,0,600)
    glClearColor(0,0,0,1)
    glClearDepth(1)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)




def loadTexture():


    textureSurface = pygame.image.load('assets/background.jpg')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)

    textures[0] = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textures[0])
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    glAlphaFunc(GL_LESS, 0.2)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    textureSurface = pygame.image.load('assets/walking.png')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)

    textures[1] = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textures[1])
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    glAlphaFunc(GL_LESS, 0.2)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    textureSurface = pygame.image.load('assets/ducking.png')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)

    textures[2] = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textures[2])
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    glAlphaFunc(GL_LESS, 0.2)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    textureSurface = pygame.image.load('assets/bird.png')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)

    textures[3] = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textures[3])
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    glAlphaFunc(GL_LESS, 0.2)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)


    textureSurface = pygame.image.load('assets/pipe.png')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)

    textures[4] = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textures[4])
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    glAlphaFunc(GL_LESS, 0.2)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    textureSurface = pygame.image.load('assets/gameover.png')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)

    textures[5] = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textures[5])
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    glAlphaFunc(GL_LESS, 0.6)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)


    return textures


def background():
    glBindTexture(GL_TEXTURE_2D, textures[0])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(0, 0, -1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(800, 0, -1)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(800,  600, -1)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(0,  600, -1)
    glEnd()
    glFlush()

class Player:
    def __init__(self,x=200,y=60,ducking=0,mass=2):
        self.x=x
        self.y=y
        self.mass=mass
        self.ducking=ducking
        self.id=0

    def jump(self):
        if(not self.ducking):
            self.y+=(2*g*200 - 2*g*(self.y-60))**0.5

    def gravity(self):
        if(self.y >= PLAYER_SIZE[1]/2):
            self.y-=((2*g*abs(self.y-260))**0.5)
        if(self.y < PLAYER_SIZE[1]/2):
            self.y=PLAYER_SIZE[1]/2

    def duck(self,v):
        if(self.y <= 60):
            self.ducking=v


    def render(self):

        if(not self.ducking):
            glBindTexture(GL_TEXTURE_2D, textures[1])
            glBegin(GL_QUADS)
            glTexCoord2f(0,0)
            glVertex(self.x-PLAYER_SIZE[0]/2, self.y-PLAYER_SIZE[1]/2, 1)
            glTexCoord2f(0,1)
            glVertex(self.x-PLAYER_SIZE[0]/2, self.y+PLAYER_SIZE[1]/2, 1)
            glTexCoord2f(1,1)
            glVertex(self.x+PLAYER_SIZE[0]/2, self.y+PLAYER_SIZE[1]/2, 1)
            glTexCoord2f(1,0)
            glVertex(self.x+PLAYER_SIZE[0]/2, self.y-PLAYER_SIZE[1]/2, 1)
            glEnd()
            glFlush()
        else:
            glBindTexture(GL_TEXTURE_2D, textures[2])
            glBegin(GL_QUADS)
            glTexCoord2f(0,0)
            glVertex(self.x-PLAYER_SIZE[0]/2, self.y-PLAYER_SIZE[1]/4 - PLAYER_SIZE[1]/4, 1)
            glTexCoord2f(0,1)
            glVertex(self.x-PLAYER_SIZE[0]/2, self.y+PLAYER_SIZE[1]/4 - PLAYER_SIZE[1]/4, 1)
            glTexCoord2f(1,1)
            glVertex(self.x+PLAYER_SIZE[0]/2, self.y+PLAYER_SIZE[1]/4 - PLAYER_SIZE[1]/4, 1)
            glTexCoord2f(1,0)
            glVertex(self.x+PLAYER_SIZE[0]/2, self.y-PLAYER_SIZE[1]/4 - PLAYER_SIZE[1]/4, 1)
            glEnd()
            glFlush()


#To define the behaviour of bird
class Bird:
    def __init__(self,x=825,y=80):
        self.x=x
        self.y=random.randint(65,y)
        self.id = 0
    def render(self):



        glBindTexture(GL_TEXTURE_2D, textures[3])
        #draw Bird  wrt to centre of its square

        glBegin(GL_QUADS)
        glTexCoord2f(0,0)
        glVertex(self.x-BIRD_SIZE[0]/2, self.y-BIRD_SIZE[1]/2, 1)
        glTexCoord2f(0,1)
        glVertex(self.x-BIRD_SIZE[0]/2, self.y+BIRD_SIZE[1]/2, 1)
        glTexCoord2f(1,1)
        glVertex(self.x+BIRD_SIZE[0]/2, self.y+BIRD_SIZE[1]/2, 1)
        glTexCoord2f(1,0)
        glVertex(self.x+BIRD_SIZE[0]/2, self.y-BIRD_SIZE[1]/2, 1)
        glEnd()

    def move(self,sx,sy):
        self.x+=sx
        self.y+=sy

#To define the behaviour of cactus
class Cacti:
    def __init__(self,x=825,y=35):
        self.x=x
        self.y=y
        self.id = 0
    def render(self):
        glBindTexture(GL_TEXTURE_2D, textures[4])
        #Draw cactus wrt to its centre
        glBegin(GL_QUADS)
        glTexCoord2f(0,0)
        glVertex(self.x-CACT_SIZE[0]/2, self.y-CACT_SIZE[1]/2, 1)
        glTexCoord2f(0,1)
        glVertex(self.x-CACT_SIZE[0]/2, self.y+CACT_SIZE[1]/2, 1)
        glTexCoord2f(1,1)
        glVertex(self.x+CACT_SIZE[0]/2, self.y+CACT_SIZE[1]/2, 1)
        glTexCoord2f(1,0)
        glVertex(self.x+CACT_SIZE[0]/2, self.y-CACT_SIZE[1]/2, 1)
        glEnd()

    def move(self,sx,sy):
        #motion of cactii
        self.x+=sx
        self.y+=sy

#function for movement of entities
def movement(entities,speed):
    for entity in entities:
        entity.move(speed[0],speed[1])
        entity.render()

#function to delete elements from a list that exceed lower limit
def remove(entities):
    for entity in entities:
        if(entity.x < 0):
            del entity


#collision functions
def collisionBird(birds,player):
    if(birds):
        for bird in birds:
            if player.x+PLAYER_SIZE[0]/2 >= bird.x-BIRD_SIZE[0]/2 and player.x-PLAYER_SIZE[0]/2 <= bird.x + BIRD_SIZE[0]/2:
                if not player.ducking:
                    if player.y+PLAYER_SIZE[1]/2 >= bird.y-BIRD_SIZE[1]/2 and player.y-PLAYER_SIZE[1]/2 <= bird.y+BIRD_SIZE[1]/2:
                        return 1

def collisionCactus(cacti,player):
    if(cacti):
        for cactus in cacti:
            if player.x+PLAYER_SIZE[0]/2 >= cactus.x-CACT_SIZE[0]/2 and player.x-PLAYER_SIZE[0]/2 <= cactus.x + CACT_SIZE[0]/2:
                if player.y-PLAYER_SIZE[1]/2 <= cactus.y+CACT_SIZE[1]/2 :
                    return 1

def gameOver():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBindTexture(GL_TEXTURE_2D, textures[5])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex(0, 0, 1)
    glTexCoord2f(1.0, 0.0)
    glVertex(800, 0, 1)
    glTexCoord2f(1.0, 1.0)
    glVertex(800,  600, 1)
    glTexCoord2f(0.0, 1.0)
    glVertex(0,  600, 1)
    glEnd()
    glFlush()
