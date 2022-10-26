# This Python file uses the following encoding: utf-8
import pygame
import math
import time

class Ai:
    velocity:float
    pos_agent = pygame.Vector2()
    vitesse_max:float
    vitesse_min:float
    initMovement:bool
    curr_time:float

    def __init__(self):
        self.image = "\assets\PNG\Survivor 1"
        pass


    def Seek(self, destination, delta_time):
        #velocity = destination - pos_agent
        #vector2.normalize * vitesse_max
        #math.min(velocity, minSpeed)
        #if initMovement :
            #lerp(initialVelocity,velocity,curr_time)
        #velocity *= delta_time
        #agent.move(velocity)


        self.velocity = destination -  self.pos_agent
        #self.pos_agent.normalize * self.vitesse_max
        pygame.math.clamp(self.velocity, self.vitesse_min ,self.vitesse_max)
        math.min(self.velocity, self.vitesse_min)
        if self.initMovement:
            math.lerp(self.initialVelocity, self.velocity, time.ctime)
        self.velocity += delta_time
        self.move(self.velocity)
        pass

    def Flee(self):
        #velocity = pos_agent - destination
        #vector2.normalize * vitesse_max
        #math.min(velocity, minSpeed)
        #if initMovement :
            #lerp(initialVelocity,velocity,curr_time)
        #velocity *= delta_time
        #agent.move(velocity)
        pass

    def Wander(self):
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
        pass

