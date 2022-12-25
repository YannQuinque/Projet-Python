##################################
# Déclaration des fonctions externes

import random
from fonctions import *

#####################################
# Corps du programme principal

if __name__ == '__main__':
    go = 0
    while go < 1 or go > 2:
        go =int(input("Commencer a jouer (Tapez 1) \nAfficher les règles du jeu (Tapez 2)"))
    if go == 2:
        print("Tetris  vous met au défi de réaliser des lignes ou des colonnes complètes en déplaçant des pièces de formes différentes adaptées au plateau choisi. \nIl vous suffit de saisir les coordonnées de l’endroit où vous voulez insérer le bloc.\nLes rangées  complétées disparaissent tout en rapportant des points et vous pouvez donc de nouveau remplir les cases libérées.")
    else:
        Forme = 0
        forme = 0
        while Forme < 1 or Forme > 4:
            Forme = int(input("Saisissez une forme de plateau:\nCercle(Tapez 1)\nLosange(Tapez 2)\nTriangle(Tapez 3)\nAléatoire(Tapez 4)\n"))
            if Forme == 1:
                forme = 'C'
            elif Forme == 2:
                forme = 'L'
            elif Forme == 3:
                forme = 'T'
            elif Forme == 4:
                forme = random.choice(['C','L','T'])
                if forme == 'C':
                    print('La forme choisie est le Carré')
                elif forme == 'L':
                    print('La forme choisie est le Losange')
                elif forme == 'T':
                    print('La forme choisie est le Triangle')

        taille = 0
        while taille < 21 or taille > 26:
            taille =int(input("Saisissez la taille de votre grille de jeu (entre 21 et 26):"))

        grille = read_grid(forme,taille)
        save_grid('grille.txt',grille)
        print_grid(grille)
