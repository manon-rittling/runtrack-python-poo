class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1
        return self.x
    
    def droite(self):
        self.x += 1
        return self.x
    
    def haut(self):
        self.y += 1
        return self.y
    
    def bas(self):
        self.y -= 1
        return self.y
    
    def position(self):
        return f"({self.x},{self.y})"

deplacement = Personnage(0, 0)

print (deplacement.position())
print(deplacement.gauche())
print(deplacement.droite())
print(deplacement.haut())
print(deplacement.bas())
print(deplacement.position())
