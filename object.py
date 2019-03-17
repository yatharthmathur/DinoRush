import pygame
import OpenGL
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import math

#game settings
DISPLAY=(800,600)
CACT_SIZE=(35,70)
CACT_SPEED=[-2.5,0]

BIRD_SIZE=(35,35)
BIRD_SPEED=[-2.5,0]

PLAYER_SIZE=(35,120)
g = 0.08
#window properties
def init():
    gluOrtho2D(0,800,0,600)
    glClearColor(1,1,1,0)

class Player:
    def __init__(self,x=200,y=60,ducking=0,mass=2):
        self.x=x
        self.y=y
        self.mass=mass
        self.ducking=ducking

    def jump(self):
        if(not self.ducking):
            self.y+=(2*g*200 - 2*g*(self.y-60))**0.5

    def gravity(self):
        if(self.y >= 60):
            self.y-=((2*g*abs(self.y-260))**0.5)
        if(self.y < 60):
            self.y=60

    def duck(self,v):
        if(self.y <= 60):
            self.ducking=v


    def render(self):
        if(not self.ducking):
            glColor(0,1,0)
            glBegin(GL_LINE_LOOP)
            glVertex(self.x-PLAYER_SIZE[0]/2, self.y-PLAYER_SIZE[1]/2)
            glVertex(self.x-PLAYER_SIZE[0]/2, self.y+PLAYER_SIZE[1]/2)
            glVertex(self.x+PLAYER_SIZE[0]/2, self.y+PLAYER_SIZE[1]/2)
            glVertex(self.x+PLAYER_SIZE[0]/2, self.y-PLAYER_SIZE[1]/2)
            glEnd()
        else:
            glColor(0,1,0)
            glBegin(GL_LINE_LOOP)
            glVertex(self.x-PLAYER_SIZE[0]/2, self.y-PLAYER_SIZE[1]/4 - 30)
            glVertex(self.x-PLAYER_SIZE[0]/2, self.y+PLAYER_SIZE[1]/4 - 30)
            glVertex(self.x+PLAYER_SIZE[0]/2, self.y+PLAYER_SIZE[1]/4 - 30)
            glVertex(self.x+PLAYER_SIZE[0]/2, self.y-PLAYER_SIZE[1]/4 - 30)
            glEnd()

#To define the behaviour of bird
class Bird:
    def __init__(self,x=825,y=150):
        self.x=x
        self.y=random.randint(115,y)
    def render(self):
        glColor(0,0,0)
        #draw Bird wrt to centre of its square
        glBegin(GL_LINE_LOOP)
        glVertex(self.x-BIRD_SIZE[0]/2, self.y-BIRD_SIZE[1]/2)
        glVertex(self.x-BIRD_SIZE[0]/2, self.y+BIRD_SIZE[1]/2)
        glVertex(self.x+BIRD_SIZE[0]/2, self.y+BIRD_SIZE[1]/2)
        glVertex(self.x+BIRD_SIZE[0]/2, self.y-BIRD_SIZE[1]/2)
        glEnd()

    def move(self,sx,sy):
        self.x+=sx
        self.y+=sy

#To define the behaviour of cactus
class Cacti:
    def __init__(self,x=825,y=35):
        self.x=x
        self.y=y
    def render(self):
        glColor(0,0,0)
        #Draw cactus wrt to its centre
        glBegin(GL_LINE_LOOP)
        glVertex(self.x-CACT_SIZE[0]/2, self.y-CACT_SIZE[1]/2)
        glVertex(self.x-CACT_SIZE[0]/2, self.y+CACT_SIZE[1]/2)
        glVertex(self.x+CACT_SIZE[0]/2, self.y+CACT_SIZE[1]/2)
        glVertex(self.x+CACT_SIZE[0]/2, self.y-CACT_SIZE[1]/2)
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

def collisionBird(birds,player):
    if(birds):
        for bird in birds:
            if player.x+PLAYER_SIZE[0]/2 >= bird.x-BIRD_SIZE[0]/2 and player.x-PLAYER_SIZE[0]/2 <= bird.x + BIRD_SIZE[0]/2:

                if not player.ducking:
                    if player.y+PLAYER_SIZE[1]/2 >= bird.y-BIRD_SIZE[1]/2 :
                        return 1

def collisionCactus(cacti,player):
    if(cacti):
        for cactus in cacti:
            if player.x+PLAYER_SIZE[0]/2 >= cactus.x-CACT_SIZE[0]/2 and player.x-PLAYER_SIZE[0]/2 <= cactus.x + CACT_SIZE[0]/2:
                if player.y-PLAYER_SIZE[1]/2 <= cactus.y+CACT_SIZE[1]/2 :
                    return 1
