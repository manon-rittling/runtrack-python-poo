import time

class joueur:
    def __init__(self, nom, numéro, position, nbButs, passesDecisives, cartonsJaunes, cartonsRouges):
        self.nom = nom
        self.numéro = numéro
        self.position = position
        self.nbButs = nbButs
        self.passesDecisives = passesDecisives
        self.cartonsJaunes = cartonsJaunes
        self.cartonsRouges = cartonsRouges

    def marquerUnBut(self):
        self.nbButs += 1
        print(f"Le joueur {self.nom} a marqué un but")

    def effectuerUnePasseDecisive(self):
        self.passesDecisives += 1
        print(f"Le joueur {self.nom} a effectué une passe décisive")

    def prendreUnCartonJaune(self):
        self.cartonsJaunes += 1
        print(f"Le joueur {self.nom} a pris un carton jaune")

    def prendreUnCartonRouge(self):
        self.cartonsRouges += 1
        print(f"Le joueur {self.nom} a pris un carton rouge")

    def afficherstatistiques(self ):
        print(f"Le joueur {self.nom} a marqué {self.nbButs} buts, a effectué {self.passesDecisives} passes décisives, a pris {self.cartonsJaunes} cartons jaunes et a pris {self.cartonsRouges} cartons rouges")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.listeJoueurs = []

    def ajouterJoueur(self, joueur):
        self.listeJoueurs.append(joueur)
        print(f"Le joueur {joueur.nom} a été ajouté à l'équipe {self.nom}")


    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques de l'équipe {self.nom}")
        for joueur in self.listeJoueurs:
            joueur.afficherstatistiques()

    
    def mettreAjourStatistiquesJoueur(self, nom, nbButs, passesDecisives, cartonsJaunes, cartonsRouges):
        for joueur in self.listeJoueurs:
            if joueur.nom == nom:
                joueur.nbButs = nbButs
                joueur.passesDecisives = passesDecisives
                joueur.cartonsJaunes = cartonsJaunes
                joueur.cartonsRouges = cartonsRouges
                print(f"Les statistiques du joueur {joueur.nom} ont été mises à jour")


    def jouerTournoi(self, equipeAdverse):
        
        print(f"Le match {self.nom} contre {equipeAdverse.nom} va commencer")
        for joueur in self.listeJoueurs:
            time.sleep(3)
            joueur.marquerUnBut()
            joueur.effectuerUnePasseDecisive()
            joueur.prendreUnCartonJaune()
            joueur.prendreUnCartonRouge()
        print(f"Le match {self.nom} contre {equipeAdverse.nom} est terminé")
        


marseille = Equipe("OM")
joueur1 = joueur("Ronaldo", 7, "Attaquant", 3, 0, 0, 0)
joueur2 = joueur("Messi", 10, "Attaquant", 7, 0, 0, 0)
joueur3 = joueur("Mbappe", 11, "Defense", 2, 1, 0, 0)
joueur4 = joueur("Pogba", 6, "Milieu", 1, 1, 1, 0)
joueur5 = joueur("Kante", 13, "Milieu", 0, 0, 1, 0)


marseille.ajouterJoueur(joueur1)
marseille.ajouterJoueur(joueur2)
marseille.ajouterJoueur(joueur3)
marseille.ajouterJoueur(joueur4)
marseille.ajouterJoueur(joueur5)


dreamTeam = Equipe("Dream Team")
joueur6 = joueur("Zidane", 10, "Milieu", 5, 2, 0, 0)
joueur7 = joueur("Henry", 12, "Attaquant", 3, 1, 0, 0)
joueur8 = joueur("Pirès", 7, "Milieu", 1, 3, 0, 0)
joueur9 = joueur("Vieira", 6, "Milieu", 0, 2, 1, 0)
joueur10 = joueur("Barthez", 1, "Gardien", 0, 0, 0, 0)


dreamTeam.ajouterJoueur(joueur6)
dreamTeam.ajouterJoueur(joueur7)
dreamTeam.ajouterJoueur(joueur8)
dreamTeam.ajouterJoueur(joueur9)
dreamTeam.ajouterJoueur(joueur10)

# presentation des joueurs
marseille.afficherStatistiquesJoueurs()
dreamTeam.afficherStatistiquesJoueurs()

marseille.jouerTournoi(dreamTeam)
# # marquer un but
# joueur1.marquerUnBut()
# joueur6.marquerUnBut()

# # carton rouge
# joueur7.prendreUnCartonRouge()

# # Afficher a jours statistiques
# marseille.afficherStatistiquesJoueurs()
# dreamTeam.afficherStatistiquesJoueurs()

