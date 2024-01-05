import random

class Carte:
    valeurs = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    figures = ['Roi', 'Reine', 'Valet']
    choixAS = [1 or 11]
    couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']

    def __init__(self, figure, valeur, couleur):
        self.figure = figure
        self.valeur = valeur
        self.couleur = couleur

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []

    def calculer_total(self):
        total = sum(carte.valeur for carte in self.main)
        as_present = (carte.valeur == 1 for carte in self.main)
        if as_present and total + 10 <= 21:
            return total + 10
        return total
    

    def afficher_main(self):
        print(f"{self.nom} Main:")
        for carte in self.main:
            print(f"{carte.figure} de {carte.couleur}")
        print(f"Total: {self.calculer_total()}\n")

    

    def prendre_carte(self, paquet):
        pioche_carte = paquet.pop()
        self.main.append(pioche_carte)
        self.afficher_main()
        # Si la carte est un As
        if pioche_carte.valeur == 1:
            pioche_carte.valeur = self.choisir_valeur_as(pioche_carte)
            

    def choisir_valeur_as(self):
        while True:
            choix = input("Voulez-vous que l'As vaille 1 ou 11? ")
            if choix.isdigit() and int(choix) in [1, 11]:
                return int(choix)
            else:
                print("Veuillez entrer une valeur valide pour l'As (1 ou 11).")


    

class JoueurHumain(Joueur):

    def prendre_carte(self, paquet):
        nouvelle_carte = paquet.pop()
        self.main.append(nouvelle_carte)
        self.afficher_main()
        # Si la carte est un As
        if nouvelle_carte.valeur == 1:
            nouvelle_carte.valeur = self.choisir_valeur_as(nouvelle_carte)





        
        
        

class Croupier(Joueur):
    def prendre_carte(self, paquet):
        while self.calculer_total() < 17:
            self.main.append(paquet.pop())

class Jeu(Carte):
    def __init__(self):
        self.paquet = self.initialiser_paquet()

    def initialiser_paquet(self):
        paquet = []

        paquet = [Carte(valeur, valeur, couleur) for valeur in Carte.valeurs for couleur in Carte.couleurs]

        # Ajouter les cartes pour les figures
        for figure in Carte.figures:
            for couleur in Carte.couleurs:
                paquet.append(Carte(figure, 10, couleur))

        # Ajouter les cartes pour les AS
        for choixAS in Carte.choixAS:
            for couleur in Carte.couleurs:
                paquet.append(Carte('As', choixAS, couleur))

        # Mélanger le paquet
        random.shuffle(paquet)
        return paquet

    def determiner_gagnant(self, joueur, croupier):
        if joueur.calculer_total() > 21:
            return "Croupier"
        elif croupier.calculer_total() > 21:
            return "Joueur"
        elif joueur.calculer_total() > croupier.calculer_total():
            return "Joueur"
        elif joueur.calculer_total() < croupier.calculer_total():
            return "Croupier"
        else:
            return "Égalité"

    def jouer(self):
        joueur = JoueurHumain("Joueur")
        croupier = Croupier("Croupier")

        joueur.main = [self.paquet.pop(), self.paquet.pop()]
        croupier.main = [self.paquet.pop(), self.paquet.pop()]

        joueur.afficher_main()
        croupier.afficher_main()

        while True:
            choix = input("Voulez-vous prendre une carte o/n? ").lower()
            if choix == 'o':
                joueur.prendre_carte(self.paquet)
                if joueur.calculer_total() > 21:
                    print("Joueur a dépassé 21. Vous avez perdu!")
                    break
            elif choix == 'n':
                break

        croupier.prendre_carte(self.paquet)

        joueur.afficher_main()
        croupier.afficher_main()

        gagnant = self.determiner_gagnant(joueur, croupier)
        print(f"Le gagnant est: {gagnant}")

# Exemple d'utilisation
jeu_blackjack = Jeu()
jeu_blackjack.jouer()
