from models.rame import Rame
from models.enum import TypeEnum, MaintenanceEnum
from controlers.Pdf_Reader import PdfReader
from controlers.Excel_maintenance import Excel_Maintenance

def main():
    pdfReadeur = PdfReader('Données sources KDM/KM_parcourus_S44-2024.pdf')
    rames = pdfReadeur.create_rame_list()
    excel = Excel_Maintenance('Données sources KDM/Copie de 12-11-2024.xlsx')
    rames = excel.setImobilisation(rames)







if __name__ == "__main__":
    main()