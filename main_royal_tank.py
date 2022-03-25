# Écrire "pip install pygame" dans la console pour installer un module (ici pygame)

import pygame

from game import Game

pygame.init()

#FPS
clock = pygame.time.Clock()
FPS = 30

# pygame.display veut dire qu'on utilise le module pygame pour l'action défini
# Créer la fenêtre du jeu
pygame.display.set_caption("Royal Tank Destructor")
screen = pygame.display.set_mode((1080, 475))  # Taille de la fenêtre (les doubles parenthèses sont importantes)
#bg = pygame.image.load('assets/images/background_map.jpg')
bg = pygame.image.load('P:/Documents/SIO_Cours_INFORMATIQUE/Developpement/Jeu_Python/RoyalTankDestructor/assets/images/background_map.jpg')

#Background du menu
#bg_menu = pygame.image.load('assets/images/background_main.jpg')
bg_menu = pygame.image.load('P:/Documents/SIO_Cours_INFORMATIQUE/Developpement/Jeu_Python/RoyalTankDestructor/assets/images/background_main.jpg')

#Bouton start
#play_button = pygame.image.load('assets/images/boutton_start.png')
play_button = pygame.image.load('P:/Documents/SIO_Cours_INFORMATIQUE/Developpement/Jeu_Python/RoyalTankDestructor/assets/images/boutton_start.png')
play_button = pygame.transform.scale(play_button, (175, 175))
play_button_rect = play_button.get_rect()
play_button_rect.x = 440
play_button_rect.y = 210

# Charge le jeu
game = Game()

running = True

# Boucle qui permet d'avoir continuellement le jeu sans qu'il se ferme
while running:

    # Appliquer l'arrière plan du jeu
    screen.blit(bg, (0, 0))


    #Jeu commencé ?
    if game.is_playing:
        #Déclencher les instructions de la partie
        game.update(screen)
    else:
        #Ajout du menu
        screen.blit(bg_menu, (-15, -140))
        screen.blit(play_button, play_button_rect)

    # Mettre à jour l'écran en continu
    pygame.display.flip()

    # Pour fermer l'application
    for event in pygame.event.get():
        # Pour que la fenêtre se ferme quand on clique sur le bouton "QUITTER"
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu.")
        # Detecter si le joueur lâche une touche du clavier
        elif event.type == pygame.KEYDOWN:  # Au cas où la touche est utilisé
            game.pressed[event.key] = True

            # Touche espace pour tirer
            if event.key == pygame.K_SPACE:
                game.tank_signature.launch_projectiles()


        elif event.type == pygame.KEYUP:  # Au cas où la touche n'est plus utilisé
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Souris sur le bouton start ?
            if play_button_rect.collidepoint(event.pos): #Souris sur le bouton
                #Mettre le jeu en mode lancer
                game.start()
#Nombre de FPS
clock.tick(FPS)