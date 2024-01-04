class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
        self.degats = 10

    def attaquer(self, cible):
        cible.vie -= self.degats
        print(f"{self.nom} attaque {cible.nom}")
        print(f"{cible.nom} a {cible.vie} points de vie")

class Jeu:
    def __init__(self):
        self.niveau = self.choisirNiveau()
         
    def choisirNiveau(self):
        niveau = input("Choisissez un niveau de difficulté : facile, moyen, difficile : ")
        print(f"Vous avez choisi le niveau {niveau}")
        return niveau

    def lancerJeu(self):
        self.joueur = Personnage("joueur", 0)  
        self.ennemi = Personnage("Ennemi", 0)  
        if self.niveau == "facile":
            self.joueur.vie = 100
            self.ennemi.vie = 50
        elif self.niveau == "moyen":
            self.joueur.vie = 50
            self.ennemi.vie = 75
        elif self.niveau == "difficile":
            self.joueur.vie = 30
            self.ennemi.vie = 100
        else:
            print("Niveau non valide")

        print(f"Vous avez {self.joueur.vie} points de vie")
        print(f"Votre ennemi a {self.ennemi.vie} points de vie")
        print("Vous êtes prêt à jouer")

    def verifierSante(self):
        if self.joueur.vie <= 0:
            print("Vous avez perdu. Game Over!")
            return False
        elif self.ennemi.vie <= 0:
            print("Félicitations! Vous avez vaincu l'ennemi. Vous avez gagné!")
            return False
        else:
            return True

    def jouerTour(self):
        self.joueur.attaquer(self.ennemi)
        self.ennemi.attaquer(self.joueur)

    def demarrerPartie(self):
        self.lancerJeu()
        while self.verifierSante():
            self.jouerTour()



jeu1 = Jeu()
jeu1.demarrerPartie()
