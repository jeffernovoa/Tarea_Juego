from character import Character
from config import ENEMY_SPEED

class Opponent(Character):
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move(self):
        self.y += ENEMY_SPEED

    def shoot(self):
        pass

    def die(self):
        self.image = self.dead_image  # Cambiar a la imagen de muerto