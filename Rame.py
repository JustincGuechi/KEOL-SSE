from Enum import TypeEnum, MaintenanceEnum

class Rame:
    def __init__ (self, numero, enum_type, enum_maintenance=MaintenanceEnum.Vide, prio_sortie=False, position=0):
        self.numero = numero
        self.enum_type = enum_type
        self.enum_maintenance = enum_maintenance
        self.prio_sortie = prio_sortie
        self.postion = position

    def getNumero(self):
        return self.numero
    def getType(self):
        return self.enum_type
    def getMaintenance(self):
        return self.enum_maintenance
    def getPrioSortie(self):
        return self.prio_sortie
    def getPosition(self):
        return self.position
    def setPosition(self, position):
        self.position = position
    def setPrioSortie(self, prio_sortie):
        self.prio_sortie = prio_sortie
    def setMaintenance(self, enum_maintenance):
        self.enum_maintenance = enum_maintenance
    