class forme:
    def aire(self):
        return 0
    
    
class Rectangle(forme):
    def __init__(self, largeur, hauteur):
        
        self.__largeur = largeur
        self.__hauteur = hauteur

    
    def aire(self):
        return self.__largeur * self.__hauteur
    

forme=forme()
print(forme.aire())


rectangle1 = Rectangle(5,10)
print(rectangle1.aire())
    
        
