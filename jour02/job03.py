class Livre:
    def __init__(self, titre, auteur, nombrePages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombrePages = int(nombrePages) if nombrePages.isdigit() and int(nombrePages) > 0 else "Erreur"
        self.__disponible = True 

    

    # Setters
    def setTitre(self, titre):
        self.__titre = titre

    def setAuteur(self, auteur):
        self.__auteur = auteur

    def setNombrePages(self, nombrePages):
        if nombrePages.isdigit() and int(nombrePages) > 0:
            self.__nombrePages = int(nombrePages)
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif. La valeur reste inchangée.")

    # Getters
    def getTitre(self):
        return self.__titre
    
    def getAuteur(self):
        return self.__auteur
    
    def getNombrePages(self):
        return self.__nombrePages
    

    def verification (self):
        if self.__disponible: 
            print("Le livre est disponible")
        else:
            print("Le livre n'est pas disponible")
        

    def emprunter (self):
        if self.__disponible:
            self.__disponible = False
            print("Le livre a été emprunté")
        else:
            print("Le livre est deja emprunté")

    
    def rendre (self):
        if not self.__disponible:
            self.__disponible = True
            print("Le livre a été rendu")
        else:
            print("Le livre est deja rendu")


livre1 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", "1000")

livre1.verification()
livre1.emprunter()
livre1.emprunter()
livre1.verification()
livre1.rendre()
livre1.verification()
livre1.emprunter()
livre1.rendre()
livre1.rendre()
















