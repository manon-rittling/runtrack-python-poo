class rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def setLongueur(self, longueur):
        self.__longueur = longueur

    def setLargeur(self, largeur):
        self.__largeur = largeur

    def getLongueur(self):
        return self.__longueur
    
    def getLargeur(self):
        return self.__largeur
    
rectangle1 = rectangle(10, 5)
print("Longueur : ", rectangle1.getLongueur())
print("Largeur : ", rectangle1.getLargeur())
rectangle1.setLongueur(7)
rectangle1.setLargeur(3)
print("Longueur : ", rectangle1.getLongueur())
print("Largeur : ", rectangle1.getLargeur())

