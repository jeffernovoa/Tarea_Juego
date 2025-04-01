import pygame as pg
from 
class character(entity):
    def __init__(self, isalive,lives=3):
        self.isalive = isalive
        self.lives = lives

    def __init__(self, isalive, lives=3,):
        self.isalive = isalive
        self.lives = lives
        self.x = x
        self.y = y

    def move(self, dirección):
        if dirección == "A":
            self.x -= 1
        elif dirección == "D":
            self.x += 1
        elif dirección == "W":
            self.y += 1
        elif dirección == "S":
            self.y += 1