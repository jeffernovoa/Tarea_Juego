import pygame
from player import Player
from opponent import Opponent
from boss import Boss
from shot import Shot

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.player = Player(400, 500)
        self.opponents = [Opponent(100, 50), Opponent(300, 50)]
        self.shots = []
        self.score = 0
        self.boss = None

    def update(self):
        self.player.move()
        for opponent in self.opponents:
            opponent.move()
        for shot in self.shots:
            shot.move()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        for opponent in self.opponents:
            opponent.draw(self.screen)
        for shot in self.shots:
            shot.draw(self.screen)