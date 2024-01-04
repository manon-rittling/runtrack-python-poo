class CompteBancaire:

    def __init__ (self, numeroCompte, nom, prenom, solde):
        self.__nom = nom
        self.__prenom = prenom
        self.__numeroCompte = numeroCompte
        self.__solde = solde
        self.__decouvert = True

    def afficher(self):
        print(f"Le compte {self.__numeroCompte} appartient {self.__prenom} {self.__nom} ")
        

    def afficherSolde(self):
        print(f"Le solde du compte bancaire de {self.__nom} {self.__prenom} est de {self.__solde} euros")
    

    def versement(self, somme):
        self.__solde = self.__solde + somme
        print(f"Le compte {self.__numeroCompte} a été crédité de {somme} euros")


    def retrait(self, sommeRetirer):
        
        if self.__decouvert == True:
            self.__solde = self.__solde - sommeRetirer

        else:
            print(f"Le compte {self.__numeroCompte} a été débité de {sommeRetirer} euros")
            print("Attention vous êtes à découvert")

    
    def interditDecouvert(self):
        self.__decouvert = False
        print(f"Le découvert est interdit pour le compte {self.__numeroCompte}")
        
    def agios(self):
        self.__solde = self.__solde - (self.__solde * 0.05)
        print(f"Le compte {self.__numeroCompte} a été débité de 5% d'agios")
        print(f"Le solde du compte {self.__numeroCompte} est de {self.__solde} euros")

    def virement(self, compteDestinataire, somme):
        self.__solde -= somme
        compteDestinataire.__solde += somme
        print(f"Le compte {self.__numeroCompte} a été débité de {somme} euros")
        print(f"Le compte {compteDestinataire.__numeroCompte} a été crédité de {somme} euros")   
    
compte1 = CompteBancaire(123456, "Dupont", "Jean", 1000)
compte2 = CompteBancaire(654321, "mougin", "sophie", -1000)

compte1.afficher()
compte1.afficherSolde()
compte1.versement(500)
compte1.afficherSolde()
compte1.retrait(2000)
compte1.agios()  
compte1.afficherSolde()

compte1.virement(compte2, 1200)

compte2.afficherSolde()        

    
        