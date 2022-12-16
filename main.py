##################################
#Déclaration des fonctions externes

import random
from functions import*

#####################################
#Corps du programme principal

if __name__=='__main__':
    go=0
    
    print("Commencer a jouer (taper 1) \nAfficher les règles du jeu (taper 2)")
    while go <1 and go <2:
        go=int(input())
    if go==2:
        print("Tetris  vous met au défi de réaliser des lignes ou des collonnes complètes en déplaçant des pièces de formes différentes adapté au plateau choisi. Il vous suffit de saisir les coordonnées de l’endroit où vous voulez insérer le bloc. Les rangées  complétées disparaissent tout en rapportant des points et vous pouvez donc de nouveau remplir les cases libérées.")

    else:
        grid=input("Saisissez une forme de plateau:\n1)cercle\n2)losange\n3)triangle\n4)Aléatoire")

    while grid<1 and grid>4:
        if grid==1:
            grid=losange
        elif grid==2:

        elif grid==3:

        elif grid==4:
