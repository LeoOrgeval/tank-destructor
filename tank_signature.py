import pygame

from projectiles import Projectiles


# Classe tank signature
class Tank_signature(
    pygame.sprite.Sprite):  # Un élément sprite est un élément graphique du jeu pouvant se déplacer (SUPER CLASSE)

    def __init__(self, game):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.all_projectiles = pygame.sprite.Group()

        self.game = game
        self.image = pygame.image.load("./assets/images/tank_signature.png")  # Lycée
        # self.image = pygame.image.load('assets/images/tank_signature.png')
        self.image = pygame.transform.scale(self.image, (124, 72))
        self.rect = self.image.get_rect()  # Position dans un "rectangle" -> La fenêtre
        self.rect.x = 80
        self.rect.y = 405

    def damage(self, amount):
        self.health -= amount

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 60, 60), [15, 20, self.max_health, 20])  # [X, Y, Largeur, Hauteur(Epaisseur)]
        pygame.draw.rect(surface, (110, 210, 40), [15, 20, self.health, 20])

    def launch_projectiles(self):
        # Nouvelle instance de la class Projectiles
        self.all_projectiles.add(Projectiles(self))

    def move_right(self):
        if self.rect.x < 200:
            self.rect.x = self.rect.x + self.velocity  # Le tank ira vers la droite (+ de coordonnées)

    def move_left(self):
        self.rect.x -= self.velocity  # Le tank ira vers la gauche (- de coordonnées)
