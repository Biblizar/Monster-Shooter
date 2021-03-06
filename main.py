import pygame
import math
from game import Game
pygame.init()

# generer la fenetre du jeu

pygame.display.set_caption("Comet Fall")
screen = pygame.display.set_mode((1080,720))

#importation de l'arrière plan
background = pygame.image.load('assets/bg.jpg')

#importer le logo
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height()/2) +40




#charger le jeu
game = Game()

running = True

#boucle d'allumage du jeu
while running:
    #appliquer l'arrière plan
    screen.blit(background, (0,-200))

    #vérification du lancement du jeu
    if game.is_playing:
        #declancher les instruction de la partie
        game.update(screen)
    #erifier si le jeu n'a pas commencé
    else:
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)

    #mettre a jour le screen
    pygame.display.flip()
    # si le joueur ferme la fenetre
    for event in pygame.event.get():

        #Verification si event est fermeture
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            #Quel touche est utilisé?
            game.pressed[event.key] = True

            #detecter si la touche espace est enclenché
            if event.key == pygame.K_SPACE:
                game.player.launch_projectil()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verification si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancé en changeant le statut de is_playing
                game.start()


