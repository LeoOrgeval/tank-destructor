import random

import pygame

from ennemy import Terrorists, Police
from tank_signature import Tank_signature


# Classe jeu
def check_collision(sprite, group):
    return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


class Game:

    def __init__(self):
        # Génère le joueur
        self.is_playing = False
        self.all_player = pygame.sprite.Group()
        self.tank_signature = Tank_signature(self)
        print(self.tank_signature.rect)
        self.all_player.add(self.tank_signature)
        # Groupe d'ennemies
        self.all_ennemy = pygame.sprite.Group()
        self.pressed = {}  # Les accolades sont un "dictionnaire"
        self.spawn_ennemy_soldier()

    def spawn_ennemy_soldier(self):
        if random.randint(1, 2) == 1:
            ennemy = Terrorists(self)
        else:
            ennemy = Police(self)
        self.all_ennemy.add(ennemy)

    def start(self):
        self.is_playing = True

    def update(self, screen):
        pass
