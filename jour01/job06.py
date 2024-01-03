class Animal:
    def __init__(self, age, prenom):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1
        return self.age
    
    def nommer(self, prenom):
        self.prenom = prenom
        return self.prenom


Animal1 = Animal(0, "")
print("L'age de l'animal initial :",Animal1.age)
print(" L'age de l'animal :", Animal1.vieillir())
print("Son nom est",Animal1.nommer("toto"))

        

        