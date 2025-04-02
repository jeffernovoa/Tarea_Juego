import pygame
from entity import Entity
from shot import Shot

class Character(Entity):
    def __init__(self, x, y, image, image_path, lives):
        self.x = x
        self.y = y
        self.image = image
        self.image_path = image_path
        self.lives = lives
        self.rect = self.image.get_rect(topleft=(x, y))

    def shoot(self):
        return Shot(self.x, self.y)

    def collide(self, other):
        return self.rect.colliderect(other.rect)