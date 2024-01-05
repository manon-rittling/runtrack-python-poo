class Personne:
    def __init__(self):
        self.age =int(14)

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self,age):
        self.age =int(age)

class Eleve(Personne):
    
    def allerEncours(self):
        print("Je vais en cours")

    def afficherAge (self):
        print(f"J'ai {self.age} ans")


class Professeur(Personne):
    def __init__(self, matiereEnseigne):
        self.__matiereEnseigne = matiereEnseigne

    def enseigner(self):
        print("Le cours va commencer")



etudiant = Eleve()
etudiant.bonjour()
etudiant.allerEncours()
etudiant.modifierAge(15)
etudiant.afficherAge()

prof = Professeur("Python")
prof.bonjour()
prof.enseigner()
prof.modifierAge(40)




    

    

    
        
    