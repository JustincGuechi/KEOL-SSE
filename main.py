from models.rame import Rame
from models.enum import TypeEnum, MaintenanceEnum
from controlers.Pdf_Reader import PdfReader
from controlers.Excel_maintenance import Excel_Maintenance
from controlers.chargementPlan import charger_excel_et_creer_plan
from controlers.algo import algo

def main():
    pdfReadeur = PdfReader('data/KM_parcourus_S44-2024.pdf')
    rames = pdfReadeur.create_rame_list()
    excel = Excel_Maintenance('data/Copie de 12-11-2024.xlsx')
    rames = excel.setImobilisation(rames)

    plan = charger_excel_et_creer_plan("data/20130304_SCH_DEX_Plan de remisage.xlsm")

    algo1 = algo(plan, rames)
    print(algo1.to_json())

if __name__ == "__main__":
    main()