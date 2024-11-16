from Rame import Rame
from Enum import TypeEnum, MaintenanceEnum
from Pdf_Reader import PdfReader
def main():
    rames = create_rame_list()


def create_rame_list():
    chemin_du_pdf = 'Données sources KDM/KM_parcourus_S44-2024.pdf'
    pdf_reader = PdfReader(chemin_du_pdf)
    tableau = pdf_reader.extraire_donnees()
    rames = []
    for ligne in tableau:
        # Type si L -> Lapin, N -> Normal, T -> Tortue en fonction de ligne[1]
        enum_type = {
            'L': TypeEnum.Lapin,
            'N': TypeEnum.Normal,
            'T': TypeEnum.Tortue
        }.get(ligne[1], TypeEnum.Normal)
        rame = Rame(
            numero=ligne[0],
            enum_type=enum_type
        )
        rames.append(rame)

    return rames



if __name__ == "__main__":
    main()