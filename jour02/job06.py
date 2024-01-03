class Commande:
    def __init__(self, numero_commande, statut_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}  
        self.__statut_commande = statut_commande

    # Setters
    def set_numero_commande(self, numero_commande):
        self.__numero_commande = numero_commande

    def set_statut_commande(self, statut_commande):
        self.__statut_commande = statut_commande

    # Getters
    def get_numero_commande(self):
        return self.__numero_commande

    def get_statut_commande(self):
        return self.__statut_commande

    # Méthode pour ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix_plat):
        self.__plats_commandes[nom_plat] = {'prix': prix_plat, 'statut': 'en cours'}
        print(f"Le plat {nom_plat} a été ajouté à la commande")

    # Méthode pour annuler un plat de la commande
    def annuler_plat(self, nom_plat):
        if nom_plat in self.__plats_commandes:
            del self.__plats_commandes[nom_plat]
            print(f"Le plat {nom_plat} a été annulé de la commande")
        else:
            print(f"Le plat {nom_plat} n'existe pas dans la commande")

    def annuler_commande(self):
        self.__plats_commandes = {}
        print("La commande a été annulée")

    # Méthode pour calculer le total de la commande 
    def __calculer_total(self):
        total = sum(plat['prix'] for plat in self.__plats_commandes.values())
        return total

    # Méthode pour afficher la commande avec le total à payer
    def afficher_commande(self):
        print(f"Commande #{self.__numero_commande}")
        for nom_plat, plat in self.__plats_commandes.items():
            print(f"{nom_plat}: {plat['prix']} € - Statut: {plat['statut']}")
        total = self.__calculer_total()
        print(f"Total à payer: {total} €")

    # Méthode pour calculer la TVA
    def calculer_tva(self, taux_tva=0.20):  # taux_tva par défaut à 20%
        total = self.__calculer_total()
        tva = total * taux_tva
        return tva
    
    def terminer_commande(self):
        self.__statut_commande = "terminée"
        print("La commande est terminée")


commande1 = Commande(1, "en cours")

commande1.ajouter_plat("Pizza", 10)
commande1.ajouter_plat("Pates", 15)
commande1.ajouter_plat("Salade", 5)
commande1.ajouter_plat("Steak", 20)


commande1.afficher_commande()
commande1.annuler_plat("Pates")
commande1.afficher_commande()
tva = commande1.calculer_tva()
print(f"TVA à payer: {tva} €")
commande1.terminer_commande()

commande2 = Commande(2, "en cours")
commande2.ajouter_plat("Pizza", 10)
commande2.ajouter_plat("Pates", 15)
commande2.ajouter_plat("frites", 5)
commande2.ajouter_plat("Steak", 20)
commande2.ajouter_plat("Salade", 5)
commande2.afficher_commande()
commande2.annuler_commande()
commande2.afficher_commande()
commande2.terminer_commande()