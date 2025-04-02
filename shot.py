import pygame
from entity import Entity
import os

class Shot(Entity):
    def __init__(self, x, y, speed, is_player_shot):
        # Cargar la imagen según el tipo de disparo
        try:
            if is_player_shot:
                image = pygame.image.load(os.path.join("assets", "shot1.png")).convert_alpha()
            else:
                image = pygame.image.load(os.path.join("assets", "shot2.png")).convert_alpha()
        except pygame.error as e:
            print(f"Error loading image: {e}")
            image = pygame.Surface((10, 10))  # Superficie predeterminada
            image.fill((255, 0, 0))  # Color rojo para visibilidad

        super().__init__(x, y, image)  # Inicializar la clase base
        self.speed = speed

    def move(self):
        # Mover el disparo en la dirección correspondiente
        self.rect.y += self.speed

    def hit_target(self, target):
        # Verificar colisión con el objetivo
        return self.rect.colliderect(target.rect)
