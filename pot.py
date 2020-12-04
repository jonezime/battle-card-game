from tkinter import *
from paquet import *


# gère le visuel des cartes du pot et la comparaison des valeurs
class Pot(Paquet):
    def __init__(self, parent, x, y):
        self.parent = parent
        self.cartes = []
        self.x, self.y = x, y

    def __lt__(self, other):
        return self.cartes[-1] < other.cartes[-1]

    def __gt__(self, other):
        return self.cartes[-1] > other.cartes[-1]

    def afficher(self):
        for position in range(len(self.cartes)):
            self.cartes[position].affiche(self.x - position,
                                          self.y - position * 30, True)


#définiton et affichage des pots
pot_gauche = Pot(tapis_jeu, 275, 125)
pot_droite = Pot(tapis_jeu, 475, 125)