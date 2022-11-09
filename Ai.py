# This Python file uses the following encoding: utf-8
import pygame
import math
import time

class Ai:
    velocity:float
    pos_agent = pygame.Vector2()
    target = pygame.Vector2()
    vitesse_max:float
    vitesse_min:float
    initMovement:bool
    curr_time:float

    def __init__(self):
        self.image = "./assets/PNG/Survivor 1/survivor1_hold.png"
        self.img = pygame.image.load(self.image)
        self.vitesse_max = 10
        self.vitesse_min = 2
        pass


    def Seek(self, delta_time):
        #velocity = destination - pos_agent
        #vector2.normalize * vitesse_max
        #math.min(velocity, minSpeed)
        #if initMovement :
            #lerp(initialVelocity,velocity,curr_time)
        #velocity *= delta_time
        #agent.move(velocity)


        self.velocity = self.target -  self.pos_agent
        self.initialVelocity = self.velocity
        #self.pos_agent.normalize * self.vitesse_max
        #pygame.math.clamp(self.velocity, self.vitesse_min ,self.vitesse_max)
        if self.velocity.length() > self.vitesse_max:
            self.velocity = self.velocity.normalize() * self.vitesse_max
        if self.initMovement():
            #(1 - time.ctime) * self.initialVelocity + time.ctime *self.velocity
                                                    #ler(Vector2, float)
            self.velocity = pygame.math.Vector2.lerp(self.pos_agent, self.velocity, delta_time)
        self.Move(self.velocity)
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

    def Move(self, velocity):
        self.pos_agent.x = velocity.x
        self.pos_agent.y = velocity.y
        pass

    def Render(self, screen):
        screen.blit(self.img, self.pos_agent)

    def behaviour(self, mode, dt):
        if(mode == 0):
            self.Seek(dt)
        if(mode == 1):
            self.Flee(dt)
        else:
            self.Wander(dt)

    def initMovement(self):
            return True




