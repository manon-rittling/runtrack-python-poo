class personne:
    def __init__(self, prenom, nom):
        self.nom = nom
        self.prenom = prenom
        
    def SePresenter(self):
        return "Bonjour, je m'appelle "+ self.prenom + " " + self.nom
        
john = personne("john", "Doe")
rija = personne("Rija", "Rakoto")


print(john.SePresenter())
print(rija.SePresenter())

        
