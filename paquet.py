from carte import *
from fenetre_jeu import *
import random


# gère le mélange des cartes, avec le rajout et la suppression (dans le pot ou la main)
class Paquet:
    def __init__(self, parent, x, y):
        self.parent = parent
        self.x, self.y = x, y
        self.cartes = []
        for i in range(4):
            for j in range(13):
                self.cartes.append(Carte(self.parent, i, j))

    def melanger(self):
        random.shuffle(self.cartes)

    def rajouter(self, carte_ajoutee):
        self.cartes.append(carte_ajoutee)

    def retirer(self):
        carte_retiree = self.cartes.pop()
        return carte_retiree


# définition du paquet
paquet = Paquet(tapis_jeu, None, None)