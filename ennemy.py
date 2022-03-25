import animation
import pygame
import random


# Class Ennemy
class Ennemy_soldier(animation.AnimationSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.game = game
        # self.image = pygame.image.load('assets/images/terrorists/png/1/run/1_terrorist_1_Run_002.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (100, 144))
        self.rect.x = 1000 + random.randint(100, 350)
        self.rect.y = 340 - offset
        self.velocity = random.randint(1, 2) / 2

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.image = pygame.image.load('./assets/images/terrorists_hurt_1_/terrorists_hurt_1_.png')
            # self.image = pygame.image.load('assets/images/terrorists/png/hurt/1_terrorist_1_Hurt_002.png')
            self.image = pygame.transform.scale(self.image, (100, 144))

            self.rect.x = 1000 + random.randint(100, 350)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health
            self.image = pygame.image.load('./assets/images/terrorists_hurt_1_/terrorists_hurt_1_.png')
            # self.image = pygame.image.load('assets/images/terrorists/png/run/1_terrorist_1_Run_002.png')
            self.image = pygame.transform.scale(self.image, (100, 144))

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 15, self.rect.y - 20, self.max_health,
                                                 5])  # [X, Y, Largeur, Hauteur(Epaisseur)]
        pygame.draw.rect(surface, (110, 210, 40), [self.rect.x + 15, self.rect.y - 20, self.health, 5])

    def forward(self):
        if self.rect.x > 700:
            self.rect.x -= self.velocity * 0.2  # Le "-=" pour que l'ennemie aille vers la gauche
        if self.rect.x <= 700:
            self.remove()
        else:
            self.image = pygame.image.load('./assets/images/terrorists_att_1_/terrorists_att_1_.png')
            # self.image = pygame.image.load('assets/images/terrorists/png/Attack1/1_terrorist_1_Attack1_002.png')
            self.image = pygame.transform.scale(self.image, (100, 144))


class Terrorists(Ennemy_soldier):

    def __init__(self, game):
        super().__init__(game, 'terrorists_run_1_', (100, 144))


class Police(Ennemy_soldier):

    def __init__(self, game):
        super().__init__(game, 'police_run_1_', (100, 144))
