from models.enum import TypeEnum, MaintenanceEnum

class Rame:
    def __init__ (self, numero, enum_type, enum_maintenance=MaintenanceEnum.Vide, prio=False, position=0, panto_or_brush=False):
        self.numero = numero
        self.enum_type = enum_type
        self.enum_maintenance = enum_maintenance
        self.prio = prio
        self.postion = position
        self.panto_or_brush = panto_or_brush

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
    def setPanto_or_brush(self, panto_or_brush):
        self.panto_or_brush = panto_or_brush
    