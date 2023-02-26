import pygame
import annex_pendu
pygame.init()

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (128, 128, 128)

# Définition de la taille de la fenêtre
TAILLE_FENETRE = (600, 170)

# Création de la fenêtre
fenetre = pygame.display.set_mode(TAILLE_FENETRE)

# Définition des boutons
BOUTON1_RECT = pygame.Rect(10, 50, 100, 50)
BOUTON2_RECT = pygame.Rect(490, 50, 100, 50)


# Boucle principale
while True:

    # Gestion des événements
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif evenement.type == pygame.MOUSEBUTTONDOWN:
            if BOUTON1_RECT.collidepoint(pygame.mouse.get_pos()):
                pygame.init(annex_pendu)
            elif BOUTON2_RECT.collidepoint(pygame.mouse.get_pos()):
                None
                # Effacement de l'écran
            fenetre.fill(BLANC)

                        # Dessin des boutons
            pygame.draw.rect(fenetre, GRIS, BOUTON1_RECT)
            pygame.draw.rect(fenetre, GRIS, BOUTON2_RECT)

                        # Affichage des textes des boutons
            font = pygame.font.SysFont(None, 24)
            text1 = font.render("Play", True, NOIR)
            text2 = font.render("Ajoutez un mot", True, NOIR)
            fenetre.blit(text1, (BOUTON1_RECT.x + 10, BOUTON1_RECT.y + 15))
            fenetre.blit(text2, (BOUTON2_RECT.x + 10, BOUTON2_RECT.y + 15))

            # Rafraîchissement de l'écran
            pygame.display.flip()

            pygame.quit()