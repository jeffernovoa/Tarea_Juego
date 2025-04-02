import pygame
import os
from character import Character

class Boss(Character):
    def __init__(self, x, y):
        try:
            # Ajusta la ruta para que apunte a la carpeta 'assets'
            image_path = os.path.join("assets", "jefe.png")
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"El archivo '{image_path}' no se encuentra.")
            image = pygame.image.load(image_path)  # Carga la imagen jefe.png
        except pygame.error as e:
            raise FileNotFoundError("No se pudo cargar la imagen 'jefe.png'. Verifica que el archivo exista.") from e
        super().__init__(x, y, image, lives=3)

    def move(self):
        self.y += 4  # Se mueve el doble de rápido que un Opponent