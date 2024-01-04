class Ville:
    def __init__ (self, nom, habitants):
        self.__nom = nom
        self.__habitants = habitants

    # Setters
    def set_nom(self, nom):
        self.__nom = nom

    def set_habitants(self, habitants):
        self.__habitants = habitants

    # Getters
    def get_nom(self):
        return self.__nom
    
    def get_habitants(self):
        return self.__habitants
    


class Personne:
    def __init__ (self, nom, age, ville ):
        self.__nom = nom
        self.__age = age
        self.__ville = ville


    # Setters
    def set_nom(self, nom):
        self.__nom = nom

    def set_age(self, age):
        self.__age = age

    def set_ville(self, ville):
        self.__ville = ville

    # Getters
        
    def get_nom(self):
        return self.__nom
    
    def get_age(self):
        return self.__age
    
    def get_ville(self):
        return self.__ville.get_nom()
    


    def ajouterPopulation(self):
        self.__nombre_habitants = self.__ville.get_habitants() + 1
        self.__ville.set_habitants(self.__nombre_habitants)
        print(f"La ville de {self.__ville.get_nom()} compte maintenant {self.__ville.get_habitants()} habitants")

    
paris = Ville("Paris", 1000000)
print(paris.get_habitants())
print(paris.get_nom())

marseille = Ville("Marseille", 861635)
print(marseille.get_habitants())
print(marseille.get_nom())

personne1= Personne("john", 45, paris)
personne1.ajouterPopulation()

personne2= Personne("Myrtille", 4, paris)
personne2.ajouterPopulation()

personne3= Personne("Chloé", 25, marseille)
personne3.ajouterPopulation()

