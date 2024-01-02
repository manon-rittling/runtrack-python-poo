class Cercle :
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, rayon):
        self.rayon= rayon
        return "le rayon est: ", self.rayon
    
    def afficherinfos(self):
        print(self.circonference())
        print(self.aire())
        print(self.diametre())
        print (f"le rayon est: {self.rayon}")

        
        
    def circonference(self):
        return "la circonference est: " + str(2*3.14*self.rayon)
    
    def aire(self):
        return "l'aire est: " + str(3.14*self.rayon**2)
    
    def diametre(self):
        return "le diametre est: " + str(2*self.rayon)
    
cercle1 = Cercle(4)
cercle1.afficherinfos()
cercle1.changerRayon(8)
cercle1.afficherinfos()

cercle2 = Cercle(7)
cercle2.afficherinfos()
cercle2.changerRayon(14)
cercle2.afficherinfos() 