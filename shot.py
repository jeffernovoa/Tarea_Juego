from entity import Entity
from config import SHOT_SPEED

class Shot(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, "assets/shot.png")

    def move(self):
        self.y -= SHOT_SPEED