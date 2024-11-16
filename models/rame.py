from models.Enum import TypeEnum, MaintenanceEnum

class Rame:
    def __init__ (self, numero, enum_type, enum_maintenance=MaintenanceEnum.Vide, prio=False, position=0):
        self.numero = numero
        self.enum_type = enum_type
        self.enum_maintenance = enum_maintenance
        self.prio = prio
        self.postion = position

    def getNumero(self):
        return self.numero
    def getType(self):
        return self.enum_type
    def getMaintenance(self):
        return self.enum_maintenance
    def getPrioSortie(self):
        return self.prio
    def getPosition(self):
        return self.position
    def setPosition(self, position):
        self.position = position
    def setPrio(self, prio):
        self.prio = prio
    def setMaintenance(self, enum_maintenance):
        self.enum_maintenance = enum_maintenance
    