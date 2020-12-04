from tkinter import *
from fenetre_jeu import *
from carte import *
from paquet import *
from affichage import *
from pot import *


def bataille():
    #affiche le nom du jeu, les mains et les pots
    def afficher_jeu():
        tapis_jeu.delete("all")
        tapis_jeu.create_text(440,
                              40,
                              text="Jeu de la bataille fermée",
                              font=("Arial", "18"))
        main_gauche.afficher()
        main_droite.afficher()
        pot_gauche.afficher()
        pot_droite.afficher()

    #gère le ramassage des cartes
    def ramasser():
        tout = pot_gauche.cartes + pot_droite.cartes
        pot_gauche.cartes = []
        pot_droite.cartes = []
        return tout

    #gère les conditions de jeu : condition de fin, qui gagne une manche et une bataille en cas d'égalité de valeurs
    def jouer():
        if ((len(main_gauche.cartes) + len(pot_gauche.cartes)) < 5
                or (len(main_droite.cartes) + len(pot_droite.cartes)) < 5):
            tapis_jeu.create_text(440,
                                  100,
                                  text=" !!! FIN !!! ",
                                  font=("Arial", "24"))
        else:
            pot_gauche.rajouter(main_gauche.retirer())
            pot_droite.rajouter(main_droite.retirer())
            afficher_jeu()

        if (pot_gauche < pot_droite):
            tapis_jeu.create_text(540,
                                  325,
                                  text="Joueur 2 gagne",
                                  font=("Arial", "12"))
            main_droite.cartes = ramasser() + main_droite.cartes
        elif (pot_gauche > pot_droite):
            tapis_jeu.create_text(335,
                                  325,
                                  text="Joueur 1 gagne",
                                  font=("Arial", "12"))
            main_gauche.cartes = ramasser() + main_gauche.cartes
        else:
            tapis_jeu.create_text(440,
                                  325,
                                  text="!!! Bataille !!!",
                                  font=("Arial", "12"))
            pot_gauche.rajouter(main_gauche.retirer())
            pot_droite.rajouter(main_droite.retirer())

    # lance la partie et active le bouton de changement de manche
    def demarrer():
        paquet.melanger()
        while len(paquet.cartes) > 0:
            main_gauche.rajouter(paquet.retirer())
            main_droite.rajouter(paquet.retirer())

        bouton_suivant.config(state="active")
        afficher_jeu()

    #affichage des boutons pour lancer une nouvelle partie et la manche suivante
    bouton_nouveau = Button(fenetre_jeu,
                            text="Nouvelle partie",
                            padx=20,
                            command=demarrer)
    bouton_nouveau.pack()
    bouton_suivant = Button(fenetre_jeu,
                            text="Manche suivante",
                            activebackground="yellow",
                            command=jouer)
    bouton_suivant.pack()
    bouton_suivant.config(state="disabled")

    fenetre_jeu.mainloop()


def main():
    bataille()
    pass


if __name__ == "__main__":
    main()