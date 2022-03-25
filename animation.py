import pygame


# Class animation
class AnimationSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name, size=(100, 144)):  # Sprite_name pour le nom de l'entité à animé
        super().__init__()
        self.size = size
        self.image = pygame.image.load(
            './assets/images/' + sprite_name + '/' + sprite_name + '.png')  # Ou (f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = animations.get(sprite_name)

    def animate(self):
        self.current_image += 1
        # Voir si on a atteint la fin de la boucle
        if self.current_image >= len(self.images):
            self.current_image = 0

        # Actualisation des images de la boucle
        self.image = self.images[self.current_image]
        self.image = pygame.transform.scale(self.image, self.size)


# Charge les images d'un sprite
def load_animation_images(sprite_name):
    # Charger les images du sprite dans le dossier correspondant
    images = []
    # Récuperation du chemin du dossier
    path = f"./assets/images/{sprite_name}/{sprite_name}"

    # Boucler sur chaque image
    for num in range(0, 5):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    return images


# Dictionnaire des images d'animations
animations = {
    'terrorists_run_1_': load_animation_images('terrorists_run_1_')
}
