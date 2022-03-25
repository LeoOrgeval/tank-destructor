import pygame


# Définir la classe qui va gérer le projectile de notre joueur
class Projectiles(pygame.sprite.Sprite):

    # Definir le constructeur
    def __init__(self, tank_signature):
        super().__init__()
        self.velocity = 4
        self.tank_signature = tank_signature
        self.image = pygame.image.load('./assets/images/projectiles_tank_missile.png')
        # self.image = pygame.image.load('assets/images/projectiles_tank_missile.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = tank_signature.rect.x + 85  # Pour que les projectiles soit lancés depuis le joueur
        self.rect.y = tank_signature.rect.y - 35
        self.image = pygame.transform.rotate(self.image, 270)
        self.origin_image = self.image  # Image dans son origine, sans rotation
        self.angle = 0

    def rotate(self):
        # Tourner le projectile
        self.angle -= 0.01
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.tank_signature.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        for ennemy in self.tank_signature.game.check_collision(self, self.tank_signature.game.all_ennemy):
            self.remove()
            ennemy.damage(self.tank_signature.attack)

        # Vérifier que les projectiles soient sorti de l'écran
        if self.rect.x > 1080:
            # Suppression du projectiles en dehors de l'écran
            self.remove()
