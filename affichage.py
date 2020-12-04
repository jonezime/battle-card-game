from tkinter import *
from paquet import *


#gère le visuel des pots de cartes et du score
class Affichage(Paquet):
    def __init__(self, parent, x, y):
        self.parent = parent
        self.x, self.y = x, y
        self.cartes = []

    def afficher(self):
        for position in range(len(self.cartes)):
            self.cartes[position].affiche(self.x, self.y, False)
            self.parent.create_text(self.x + 50,
                                    self.y - 35,
                                    text="Score : " + str(len(self.cartes)),
                                    font=("Arial", "16"))


main_gauche = Affichage(tapis_jeu, 100, 125)
main_droite = Affichage(tapis_jeu, 650, 125)