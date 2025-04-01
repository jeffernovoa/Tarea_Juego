import pygame
from entity import Entity

class Shot(Entity):
    def __init__(self, game, character, is_player_shot=True):
        # Calcular dimensiones del disparo
        size = int(game.width * 0.015)
        width, height = size, size

        # Calcular posición inicial del disparo
        x = character.x + character.width // 2 - width // 2
        y = character.y

        # Configurar velocidad y ruta de la imagen según el tipo de disparo
        speed = -10 if is_player_shot else 10
        image_path = 'assets/shot1.png' if is_player_shot else 'assets/shot2.png'

        # Inicializar la clase base
        super().__init__(game, width, height, x, y, speed, image_path)
        self.is_player_shot = is_player_shot

    def update(self):
        # Actualizar posición del disparo
        self.y += self.speed

        # Eliminar el disparo si sale de la pantalla
        if not (0 <= self.y <= self.game.height):
            self.remove_from_game()

    def remove_from_game(self):
        # Obtener la lista correspondiente de disparos y eliminar el disparo actual
        shot_list = self.game.player_shots if self.is_player_shot else self.game.opponent_shots
        shot_list.discard(self)  # Usar discard para evitar errores si no está en la lista

    def __str__(self):
        return f"{super().__str__()} (SHOT)"
