import pygame
from random import choice


# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (128, 128, 128)

# Définition de la taille de la fenêtre
TAILLE_FENETRE = (600, 170)

# Création de la fenêtre
fenetre = pygame.display.set_mode(TAILLE_FENETRE)

erreur = 0
noELementDessin = 0

victoire = False



myfile = "mots.txt"
 
def random_word(myfile):
    with open(myfile, 'r') as f: 
        word_list = f.read().splitlines() # Dans le cas d'un fichier où il y a un mot par ligne 
        random_w = choice(word_list)
     
    return random_w

mot_a_trouver = random_word(myfile)
tailleMotAtrouver = len(mot_a_trouver)
proposition = "_" * tailleMotAtrouver

font = pygame.font.Font(None, 36) # Définition de la police d'écriture


dessins = [
    [10, 10, 210, 10],
    [110, 10, 110, 390],
    [105, 390, 240, 390],
    [110, 340, 160, 390],
    [230, 390, 230, 300],
    [210, 300, 250, 300, 250, 260, 210, 260, 210, 300],
    [230, 260, 230, 250, 180, 250, 280, 250],
    [200, 150, 230, 250, 260, 150],
]

maxErreurs = len(dessins)

def genererCoordonnees(cs):
    drapeau = True

    ncs = []

    return ncs