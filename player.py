from character import Character
import pygame
from config import PLAYER_SPEED, SCREEN_WIDTH

class Player(Character):
    def __init__(self, x, y):
        super().__init__(x, y, "assets/player.png", 3)
        self.score = 0
        self.lives = 3
        self.bullets = []  # Lista para manejar las balas del jugador

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:  # Evitar salir por la izquierda
            self.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.width:  # Evitar salir por la derecha
            self.x += PLAYER_SPEED

    def shoot(self):
        # Implementación básica de disparo
        bullet = Bullet(self.x + self.width // 2, self.y)  # Crear un proyectil
        self.bullets.append(bullet)  # Añadirlo a la lista de balas del jugador