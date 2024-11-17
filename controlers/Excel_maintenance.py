import pandas as pd
from models.rame import Rame
from models.enum import MaintenanceEnum
class Excel_Maintenance:
    def __init__(self, path):
        self.path = path
        self.df = pd.read_excel(self.path)
        first_Dx = [7, 1]
        self.first_Dx = self.df.iat[first_Dx[0], first_Dx[1]]
        Dx = [first_Dx[0]+ 1 + i for i in range(7)]
        self.Dx = [self.df.iat[Dx[i], first_Dx[1]] for i in range(7)]
        Imo = [Dx[-1] + 1 + i for i in range(8)]
        self.Imo = [self.df.iat[Imo[i], first_Dx[1]] for i in range(8)]
        maintenance = [Imo[-1] + 1 + i for i in range(7)]
        self.maintenance = [self.df.iat[maintenance[i], first_Dx[1]] for i in range(7)]
        panto_or_brush = [maintenance[-1] + 4 + i for i in range(7)]
        list_panto_or_brush = [self.df.iat[panto_or_brush[i], first_Dx[1]]for i in range(7)]
        self.panto_or_brush = []
        for panto in list_panto_or_brush:
            if isinstance(panto, str):
                self.panto_or_brush.append(int(panto.split(" ")[0]))


    def setImobilisation(self, rames):
        for rame in rames:
            if rame.numero == self.first_Dx:
                rame.setMaintenance(MaintenanceEnum.Dx)
                rame.setPrio(True)
            elif rame.numero in self.Dx:
                rame.setMaintenance(MaintenanceEnum.Dx)
            elif rame.numero in self.Imo:
                rame.setMaintenance(MaintenanceEnum.Imo)
            elif rame.numero in self.maintenance:
                rame.setMaintenance(MaintenanceEnum.Maintenance)
            elif rame.numero in self.panto_or_brush:
                rame.setPanto_or_brush(True)
        return rames