import pygame
from character import Character

WIDTH, HEIGHT = 800, 600

class Player(Character):
    def __init__(self, x, y, image_path="assets/bueno.png"):
        try:
            # Carga la imagen desde la ruta proporcionada
            image = pygame.image.load(image_path).convert_alpha()
        except FileNotFoundError:
            print(f"Error: El archivo '{image_path}' no se encontró. Usando un reemplazo temporal.")
            # Crea un reemplazo temporal si la imagen no se encuentra
            image = pygame.Surface((40, 40))
            image.fill((255, 255, 255))  # Llena el reemplazo con un color blanco
        # Llama al constructor de la clase base con todos los argumentos requeridos
        super().__init__(x, y, image, image_path, lives=3)
        self.score = 0

    def move(self, dx, dy):
        new_x = max(0, min(WIDTH - self.image.get_width(), self.x + dx))
        new_y = max(0, min(HEIGHT - self.image.get_height(), self.y + dy))
        self.x, self.y = new_x, new_y

    def shoot(self):
        # Crea un disparo que se mueve hacia arriba
        return Shot(self.x + self.image.get_width() // 2, self.y, -10, True)