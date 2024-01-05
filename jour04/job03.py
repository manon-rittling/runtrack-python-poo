class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    

# setters
    
    def setLongueur(self, longueur):
        self.__longueur = longueur

    def setLargeur(self, largeur):
        self.__largeur = largeur

# getters
        
    def getLongueur(self):
        return self.__longueur
    
    def getLargeur(self):
        return self.__largeur
    

class Parallelepipede(Rectangle):
    def __init__(self,hauteur, longueur, largeur):
        self.__hauteur = hauteur
        Rectangle.__init__(self, longueur, largeur)

    def volume(self):
        return self.__hauteur * self.getLargeur() * self.getLongueur()
    
    def setHauteur(self, hauteur):
        self.__hauteur = hauteur

    def getHauteur(self):
        return self.__hauteur
    

rectangle1=Rectangle(5,10)
print(rectangle1.surface())
print(rectangle1.perimetre())
rectangle1.setLongueur(7)
rectangle1.setLargeur(14)
print(rectangle1.getLargeur())
print(rectangle1.getLongueur())

parallelepipede1=Parallelepipede(5,10,15)