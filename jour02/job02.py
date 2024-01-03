class Livre:
    def __init__(self, titre, auteur, nombrePages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombrePages = int(nombrePages) if nombrePages.isdigit() and int(nombrePages) > 0 else "Erreur"

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


livre1 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", "-1000")

# Afficher les attributs initiaux
print("Titre : ", livre1.getTitre())
print("Auteur : ", livre1.getAuteur())
print("Nombre de pages : ", livre1.getNombrePages())

# Modifier les attributs avec les setters
livre1.setTitre("Harry Potter")
livre1.setAuteur("J.K. Rowling")
livre1.setNombrePages("500")  

# Afficher les attributs mis à jour
print("Titre mis à jour : ", livre1.getTitre())
print("Auteur mis à jour : ", livre1.getAuteur())
print("Nombre de pages mis à jour : ", livre1.getNombrePages())
