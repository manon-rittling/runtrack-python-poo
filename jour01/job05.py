class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLespoints(self):
        return f'les coordonnées sont: {self.x} , {self.y}' 
    
    def afficherX(self):
        return f"x =  {self.x}"
    
    def afficherY(self):
        return f"y =  {self.y}"
    
    def changerX(self, x):
        self.x = x
        return f"x =  {self.x}"
    
    def changerY(self, y):
        self.y = y
        return f"y =  {self.y}"
    

valeur = Point(1, 2)

print(valeur.afficherLespoints())
print(valeur.afficherX())
print(valeur.afficherY())
print(valeur.changerX(3))
print(valeur.changerY(4))
print(valeur.afficherLespoints())
