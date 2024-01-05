class Tache:
    def __init__(self, titre, description, statut):
        self.__titre = titre
        self.__description = description
        self.__statut = "à faire" or "terminé" 

    # Setters
    def set_titre(self, titre):
        self.__titre = titre

    def set_description(self, description):
        self.__description = description

    def set_statut(self, statut):
        self.__statut = statut

    # Getters
        
    def get_titre(self):
        return self.__titre
    
    def get_description(self):
        return self.__description
    
    def get_statut(self):
        return self.__statut
    

class ListeDeTaches:
    def __init__(self, titre):
        self.titre = titre
        self.listTaches = []

    # Setters
    def set_listTaches(self, listTaches):
        self.listTaches = listTaches

    # Getters
    def get_listTaches(self):
        return self.listTaches
    

    def ajouter_tache(self, tache):
        self.listTaches.append(tache)
        print(f"La tâche {tache.get_titre()} a été ajoutée à la liste")

    def supprimer_tache(self, tache):
        self.listTaches.remove(tache)
        print(f"La tâche {tache.get_titre()} a été supprimée de la liste")

    def marquerCommeFinie(self, tache):
        tache.set_statut("terminé")
        print(f"   -La tâche {tache.get_titre()} a été marquée comme terminée")

    
    def afficherListe(self):
        print(f"Liste des tâches de la liste: {self.titre} ")
        for tache in self.listTaches:
            print(f"{tache.get_titre()} - {tache.get_description()} - {tache.get_statut()}")

    
    def filtrerListe(self, statut):
        for tache in self.listTaches:
            if tache.get_statut() == statut:
                print(f"   -{tache.get_titre()} - {tache.get_description()} - {tache.get_statut()}")


tache1 = Tache("Faire les courses", "Acheter du pain, du lait et des oeufs", "à faire")
tache2 = Tache("Faire la vaisselle", "Ne pas oublier de laver les verres", "à faire")
tache3 = Tache("Faire la lessive", "Ne pas oublier d'ajouter de l'adoucissant", "terminé")
tache4 = Tache("Faire le ménage", "Ne pas oublier de passer l'aspirateur", "terminé")



liste = ListeDeTaches("To Do List")
liste.ajouter_tache(tache1)
liste.ajouter_tache(tache2)
liste.ajouter_tache(tache3)
liste.ajouter_tache(tache4)
liste.afficherListe()

liste.supprimer_tache(tache1)

liste.marquerCommeFinie(tache2)

liste.afficherListe()
liste.filtrerListe("à faire")



