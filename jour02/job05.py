class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.en_marche = False
        self.__reservoir = 50

    # Setters
    
    def setMarque(self, marque):
        self.__marque = marque

    def setModele(self, modele):
        self.__modele = modele

    def setAnnee(self, annee):
        self.__annee = annee

    def setKilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def setReservoir(self, reservoir):
        self.__reservoir = reservoir

    # Getters
    def getMarque(self):
        return self.__marque
    
    def getModele(self):
        return self.__modele
    
    def getAnnee(self):
        return self.__annee
    
    def getKilometrage(self):
        return self.__kilometrage
    
    def getReservoir(self):
        return self.__reservoir
    
    def get_en_marche(self):
        return self.en_marche
    

    
    # methode pour demarrer change valeur attribut en True
    def demarrer(self):
        
        if self.__verifier_plein():
            self.en_marche = True
            print("La voiture est demarrée")
        else:
            print("La voiture n'a pas assez d'essence pour démarrer")

    # methode pour arreter change valeur attribut en False
    def arreter(self):
        self.en_marche = False
        print("La voiture est arretée")


    def __verifier_plein(self):
        return self.__reservoir > 5 
    


voiture1 = Voiture("Peugeot", "208", "2019", "1000")

print("Marque : ", voiture1.getMarque())
print("Modele : ", voiture1.getModele())
print("Année : ", voiture1.getAnnee())
print("Kilometrage : ", voiture1.getKilometrage())


voiture1.demarrer()
voiture1.arreter()
voiture1.setKilometrage("20000")
voiture1.setReservoir(5)
voiture1.get_en_marche()
voiture1.demarrer()

