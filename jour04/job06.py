class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    
    def informationsVehicules(self):
        print(f"Marque : {self.marque}")
        print(f"Modele : {self.modele}")
        print(f"Annee : {self.annee}")
        print(f"Prix : {self.prix}")

    def demarrer(self):
        print("Attention, je roule!")


class Voiture(Vehicule):
    def __init__(self):
        self.portes = 4
        
    def informationsVehicule(self):
        super().informationsVehicules()
        print(f"Portes : {self.portes}")

    
voiture=Voiture()
voiture.marque="mercedes"
voiture.modele="classe A"
voiture.annee="2020"
voiture.prix="30000"
voiture.informationsVehicule()
voiture.demarrer()

class Moto(Vehicule):
    def __init__(self):
        self.roues = 2

    def informationsVehicule(self):
        super().informationsVehicules()
        print(f"Roues : {self.roues}")

moto=Moto()
moto.marque="yamaha"
moto.modele="r1"
moto.annee="2020"
moto.prix="15000"
moto.informationsVehicule()
moto.demarrer()

    
