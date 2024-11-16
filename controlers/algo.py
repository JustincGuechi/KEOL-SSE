from models.plan import Plan
from models.rame import Rame
from models.place import Place
from models.enum import TypeEnum, MaintenanceEnum
from datetime import datetime

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


    def run(self):
        list_pop = []

        for rame in self.rames:
            if rame.enum_maintenance == MaintenanceEnum.Imo or rame.enum_maintenance == MaintenanceEnum.Maintenance:
                list_pop.append(self.rames.pop(self.rames.index(rame)))


        self.rames.sort(key=lambda x: x.enum_type.value)
        self.rames.sort(key=lambda x: x.prio, reverse=True)
        self.rames.sort(key=lambda x: x.panto_or_brush, reverse=True)

        # trouver la place avec l'heure de retour la plus tot
        self.plan.places
        min = "03:00:00:00"
        index = 0
        for i in range (len(self.plan.places)):
            if self.plan.places[i].horaire_arrivee != '':
                if self.plan.places[i].horaire_arrivee < min:
                    index = i
                    min = self.plan.places[i].horaire_arrivee
        
        return self.plan