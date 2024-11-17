from models.plan import Plan
from models.rame import Rame
from models.place import Place
from models.enum import TypeEnum, MaintenanceEnum
from datetime import datetime
from datetime import timedelta

class algo:
    def __init__(self, plan, rames):
        if not isinstance(plan, Plan):
            raise TypeError("The object added must be an instance of the Plan class.")
        if not isinstance(rames, list):
            raise TypeError("The object added must be a list of rames.")
        for rame in rames:
            if not isinstance(rame, Rame):
                raise TypeError("The object added must be an instance of the Rame class.")
        self.plan = plan
        self.rames = rames
        self.run()

    def soustraction_heure(self, heure1, heure2):
        heure1 = datetime.strptime(heure1, '%d:%H:%M:%S')
        heure2 = datetime.strptime(heure2, '%d:%H:%M:%S')
        return heure1 - heure2
    
    def run(self):
        list_pop = []
        tab = []

        for rame in self.rames:
            if rame.enum_maintenance == MaintenanceEnum.Imo or rame.enum_maintenance == MaintenanceEnum.Maintenance:
                list_pop.append(self.rames.pop(self.rames.index(rame)))


        self.rames.sort(key=lambda x: x.enum_type.value)
        self.rames.sort(key=lambda x: x.prio, reverse=True)
        self.rames.sort(key=lambda x: x.panto_or_brush, reverse=True)

        # trouver la place avec l'heure de retour la plus tot
        min = "03:00:00:00"
        index = 0
        for i in range (len(self.plan.places)):
            if self.plan.places[i].horaire_arrivee != '':
                if self.plan.places[i].horaire_arrivee < min:
                    index = i
                    min = self.plan.places[i].horaire_arrivee
        for rame in self.rames:
            if rame.enum_maintenance == MaintenanceEnum.Dx and rame.prio == True:
                self.plan.places[index].rame=self.rames.pop(self.rames.index(rame))
                tab.append(index)
                break
        # get la liste de rame qui on un type Dx
        list_dx = []
        for rame in self.rames:
            if rame.enum_maintenance == MaintenanceEnum.Dx:
                list_dx.append(rame)
        # remplir les places avec les rames de type Dx par la fin en sautant les places deja rempli
        for rame in list_dx:
            for i in range (len(self.plan.places)-1, 0, -1):
                if i not in tab:
                    if self.plan.places[i].horaire_arrivee != '':
                        self.plan.places[i].rame=self.rames.pop(self.rames.index(rame))
                        tab.append(i)
                        break
        #remplie avec les rames qui ont des bruch ou panto sachant qu'il faut au moins une sur ligne_id 1 et 2 et plus grande plage horaire possible
        departT1 = "03:00:00:00"
        index1 = 0
        departT2 = "03:00:00:00"
        index2 = 0
        for i in range (0,15):
            print(self.plan.places[i].ligne_id)

            if self.plan.places[i].horaire_arrivee != '' and self.plan.places[i].horaire_depart != '':
                if self.plan.places[i].ligne_id.startswith('91'):
                    if self.plan.places[i].horaire_depart < departT1:
                        departT1 = self.plan.places[i].horaire_depart
                        index1 = i
                if self.plan.places[i].ligne_id.startswith('92'):
                    if self.plan.places[i].horaire_depart < departT2:
                        departT2 = self.plan.places[i].horaire_depart
                        index2 = i 
        #PROBLEME AVEC LE 9211 qui est a 00:00:00:00
        print(departT1)
        print(departT2)
        print(index1)
        print(index2)
        
        #on place les rames avec panto ou brush sur les lignes 1 et 2
        self.plan.places[index1].rame=self.rames.pop(0)
        self.plan.places[index2].rame=self.rames.pop(0)
        tab.append(index1)
        tab.append(index2)

        #remplir les places avec les rames qui reste en commencant par les rames de type lapin
        self.rames.sort(key=lambda x: x.enum_type.value)
        print(len(self.plan.places))
        print(len(self.rames))
        print(len(tab))
        memoire_tempon = self.rames.copy()
        for rame in memoire_tempon:
            print(rame.numero)
            for i in range(len(self.plan.places)):
                if i not in tab:
                    if self.plan.places[i].horaire_depart != '':
                        self.plan.places[i].rame = self.rames.pop(self.rames.index(rame))
                        print("La rame " + str(rame) + " a ete placee a la place " + str(i))
                        tab.append(i)
                        break
        
       
        
        memoire_tempon_R7 = self.rames.copy()
        for rame in memoire_tempon_R7:
            for i in range (5):
                if i not in tab:
                    self.plan.places[i].rame = self.rames.pop(self.rames.index(rame))
                    tab.append(i)
                    break

        #test si toutes les places sont remplies
        for i in range (len(self.plan.places)):
            if self.plan.places[i].rame == 0 :
                print("La place " + str(i) + " n'est pas remplie")
        return self.plan