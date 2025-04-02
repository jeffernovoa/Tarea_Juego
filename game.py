import pygame
import random
from player import Player
from opponent import Opponent
from boss import Boss

pygame.init()  # Inicializar Pygame

# Configuración de la pantalla y constantes
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

class Game:
    def __init__(self):
        self.is_running = True
        self.score = 0
        self.player = Player(WIDTH // 2, HEIGHT - 50, "assets/bueno.png")
        self.player.image.fill((0, 255, 0))  # Color verde para el jugador
        self.opponent = Opponent(random.randint(0, WIDTH - 40), 50, pygame.Surface((40, 40)))
        self.opponent.image.fill((255, 0, 0))  # Color rojo para el oponente
        self.boss = None
        self.shots = []

    def start(self):
        while self.is_running:
            self.handle_events()
            self.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        screen.fill((0, 0, 0))  # Limpia la pantalla con un color negro

        # Manejo de entrada del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(-5, 0)
        if keys[pygame.K_RIGHT]:
            self.player.move(5, 0)
        if keys[pygame.K_SPACE]:
            new_shot = self.player.shoot()
            if new_shot:  # Asegúrate de que el disparo no sea None
                self.shots.append(new_shot)

        # Movimiento del oponente
        self.opponent.move()
        if random.randint(0, 50) == 1:  # Probabilidad de disparo del oponente
            new_shot = self.opponent.shoot()
            if new_shot:
                self.shots.append(new_shot)

        # Movimiento del jefe (si existe)
        if self.boss:
            self.boss.move()
            if random.randint(0, 30) == 1:  # Probabilidad de disparo del jefe
                new_shot = self.boss.shoot()
                if new_shot:
                    self.shots.append(new_shot)

        # Manejo de disparos
        for shot in self.shots[:]:  # Itera sobre una copia de la lista para evitar problemas al eliminar elementos
            if shot:  # Asegúrate de que el disparo no sea None
                shot.move()
                # Elimina disparos fuera de la pantalla
                if shot.y < 0 or shot.y > HEIGHT:
                    self.shots.remove(shot)
                    continue

                # Verifica colisiones con el oponente
                if shot.hit_target(self.opponent):
                    self.score += 1
                    if not self.boss:  # Si no hay jefe, crea uno
                        self.boss = Boss(random.randint(0, WIDTH - 60), 50, pygame.Surface((60, 60)))
                        self.boss.image.fill((255, 255, 0))  # Color amarillo para el jefe
                    self.opponent.y = 0
                    self.opponent.x = random.randint(0, WIDTH - 40)
                    self.shots.remove(shot)
                    continue

                # Verifica colisiones con el jefe
                if self.boss and shot.hit_target(self.boss):
                    self.boss.lives -= 1
                    if self.boss.lives <= 0:  # Si el jefe es derrotado
                        self.boss = None
                        self.end_game(victory=True)
                    self.shots.remove(shot)
                    continue

                # Verifica colisiones con el jugador
                if shot.hit_target(self.player):
                    self.player.lives -= 1
                    if self.player.lives <= 0:  # Si el jugador pierde todas las vidas
                        self.end_game(victory=False)
                    self.shots.remove(shot)
                    continue

        # Dibuja los elementos en pantalla
        self.player.draw(screen)
        self.opponent.draw(screen)
        if self.boss:
            self.boss.draw(screen)
        for shot in self.shots:
            if shot:  # Asegúrate de que el disparo no sea None
                shot.draw(screen)

        # Muestra el puntaje y las vidas
        self.display_score_lives()

        # Actualiza la pantalla
        pygame.display.flip()
        clock.tick(30)  # Controla la velocidad del juego

    def display_score_lives(self):
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        lives_text = font.render(f"Lives: {self.player.lives}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 40))

    def end_game(self, victory):
        self.is_running = False
        if victory:
            print("Congratulations! You defeated the Boss!")
        else:
            print("Game Over")