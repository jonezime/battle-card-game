from tkinter import *


# gère le visuel des cartes jouées et la comparaison des valeurs
class Carte:
    nom_couleur = ["trefle", "carreau", "coeur", "pique"]
    nom_valeur = [
        "as", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valet", "dame",
        "roi"
    ]
    dos_carte = PhotoImage(file="assets/dos_carte.gif")

    def __init__(self, parent, couleur, valeur):
        self.parent = parent
        self.couleur = couleur
        self.valeur = valeur
        self.image = PhotoImage(file="assets/" +
                                Carte.nom_valeur[self.valeur] + "_" +
                                Carte.nom_couleur[self.couleur] + ".gif")

    def affiche(self, x, y, sens):
        if sens:
            self.parent.create_image(x, y, anchor=NW, image=self.image)
        else:
            self.parent.create_image(x, y, anchor=NW, image=Carte.dos_carte)

    def __lt__(self, adversaire):
        a = self.valeur
        b = adversaire.valeur
        if (a == 0):
            a = 13
        if (b == 0):
            b = 13
        return a < b

    def __gt__(self, adversaire):
        a = self.valeur
        b = adversaire.valeur
        if (a == 0):
            a = 13
        if (b == 0):
            b = 13
        return a > adversaire.valeur