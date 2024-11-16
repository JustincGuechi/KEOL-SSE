from enum import Enum

class TypeEnum(Enum):
    Lapin = 1
    Normal = 2
    Tortue = 3

class MaintenanceEnum(Enum):
    Dx = 1
    Imo = 2
    Maintenance = 3
    Vide = 4

class Type_Place(Enum):
    RAME = 1
    RAME_IMMOBILISEE = 2
    NO_RAME = 3