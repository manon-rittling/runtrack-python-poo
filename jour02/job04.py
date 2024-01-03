class Student:
    def __init__(self, nom, prenom, id, nbreCredits):
        self.nom = nom
        self.prenom = prenom
        self.id = id
        self.nbreCredits = nbreCredits
        self.__level = self.__studentEval()

    def set_add_credits(self, credits):
         
        if self.nbreCredits > 0:
            self.nbreCredits += credits
            self.__level = self.__studentEval()
        else:
            print("Le nombre de crédits ne peut pas être négatif. La valeur est mise à 0.")
        

    # getters
    def getNom(self):
        return self.nom
    
    def getPrenom(self):
        return self.prenom
    
    def getId(self):
        return self.id
    
    def getNbreCredits(self):
        return self.nbreCredits
    
    def get_afficher(self):
        print (f"Le nombre de credits de , {self.nom} {self.prenom} est de {self.nbreCredits} crédits")
        

    def __studentEval(self):
        if self.nbreCredits >= 90:
            return "Excellent"
        elif self.nbreCredits >= 80:
            return "Très bien"
        elif self.nbreCredits >= 70:
            return "Bien"
        elif self.nbreCredits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
        

    def studentInfo(self):
        print("Nom : ", self.nom)
        print("Prénom : ", self.prenom)
        print("ID : ", self.id)
        print("Niveau : ", self.__level)
        


etudiant1 = Student("Doe", "john", "145", 20)


etudiant1.get_afficher()
etudiant1.set_add_credits(-10)
etudiant1.set_add_credits(90)
etudiant1.set_add_credits(12)
print("Nombre de crédits : ", etudiant1.getNbreCredits())
etudiant1.studentInfo()
etudiant1._Student__studentEval()


etudiant2 = Student("dupont", "jane", "146", 80)
etudiant2.get_afficher()
etudiant2.studentInfo()
print("Nombre de crédits : ", etudiant2.getNbreCredits())
etudiant2._Student__studentEval()


etudiant3 = Student("duuk", "lisa", "148", 40)

etudiant3._Student__studentEval()
etudiant3.get_afficher()
etudiant3.studentInfo()




