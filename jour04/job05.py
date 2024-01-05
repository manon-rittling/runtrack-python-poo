class forme:
    def aire(self):
        return 0
    

class cercle(forme):
    def __init__(self, rayon):
        self.__rayon = rayon
    
    def aire(self):
        return 3.14 * self.__rayon ** 2
    
class Rectangle(forme):
    def __init__(self, largeur, hauteur):
        
        self.__largeur = largeur
        self.__hauteur = hauteur

    
    def aire(self):
        return self.__largeur * self.__hauteur
    

cercle1 = cercle(13)
print(cercle1.aire())

rectangle1 = Rectangle(5,10)
print(rectangle1.aire())