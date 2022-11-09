# This Python file uses the following encoding: utf-8
import pygame
import math
import time

class Ai:
    velocity:float
    pos_agent:pygame.Rect = None
    target = pygame.Vector2()
    vitesse_max:float
    vitesse_min:float
    initMovement:bool
    curr_time:float
    initTime = None
    atDestination = False

    def __init__(self):
        self.image = "./assets/PNG/Survivor 1/survivor1_hold.png"
        self.img = pygame.image.load(self.image)
        self.vitesse_max = 15
        self.vitesse_min = 2
        self.pos_agent = self.img.get_rect()
        pass


    def Seek(self, delta_time):
        #if (time.time() - self.initTime) / 5 >= 1:
            #self.atDestination = True
        if self.atDestination == False:
            self.velocity = self.target -  pygame.Vector2(self.pos_agent.x,self.pos_agent.y)
            if self.vitesse_max == self.velocity.length():
                self.initTime = None
                self.atDestination = True
                print(self.atDestination)
            if self.velocity.length() > self.vitesse_max:
                self.velocity = self.velocity.normalize() * self.vitesse_max
            if self.initMovement() and self.vitesse_max > self.velocity.length():
                self.initTime = time.time()
            if self.initTime != None:
                self.velocity = pygame.math.Vector2.lerp(pygame.Vector2(0,0), self.velocity, (time.time() - self.initTime) / 5)

            self.pos_agent = self.pos_agent.move(self.velocity)
            pass

    def Flee(self, delta_time):
        #velocity = pos_agent - destination
        #vector2.normalize * vitesse_max
        #math.min(velocity, minSpeed)
        #if initMovement :
            #lerp(initialVelocity,velocity,curr_time)
        #velocity *= delta_time
        #agent.move(velocity)
        pass

    def Wander(self, delta_time):
        #if agent_pos != destination
            #destination = angle.as_vector() * distanceToMove + agent_pos
            #angle += random() - random() fait en sorte d'avoir une valeur entre -1 et 1
        #vector2.normalize * vitesse_max
        #math.min(velocity, minSpeed)
        #if initMovement :
            #lerp(initialVelocity,velocity,curr_time)
        #velocity *= delta_time
        #agent.move(velocity)
        #formule pour savoir ou il va:
            #(x,y) = (cos0, sin0)
        pass

    def Render(self, screen):
        print(self.pos_agent)
        screen.blit(self.img, self.pos_agent)

    def behaviour(self, mode, dt):
        if(mode == 0):
            self.Seek(dt)
        if(mode == 1):
            self.Flee(dt)
        else:
            self.Wander(dt)

    def initMovement(self):
            return self.initTime == None




