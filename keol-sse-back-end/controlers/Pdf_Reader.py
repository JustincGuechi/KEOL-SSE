#Ce fichier sera utiliser pour l'extraction des données d'un pdf 
#Le pdf doit etre sous forme de tableau avec seulement le tableau sur la page (avec les entetes de colonnes suivant dans l'ordre :
#N°rame | Type | Kilometrage rame | KM de la semaine dernière | Remarque
#Et des données sous la forme suivante :
#1003 | L | 836334 | 1731 | OK


import pdfplumber
from models.enum import TypeEnum, MaintenanceEnum
from models.rame import Rame


class PdfReader:
    def __init__(self, chemin_du_pdf):
        self.chemin_du_pdf = chemin_du_pdf
        #Tableau des données extraites du PDF (format : [Num_ram,Type,Remaque])
        self.tableau = []

    def extraire_donnees(self):
        # Lire le contenu du PDF
        with pdfplumber.open(self.chemin_du_pdf) as pdf:
            for num_page, page in enumerate(pdf.pages):
                texte = page.extract_text()
                lignes = texte.split('\n')
                for ligne in lignes:

                    # Si la ligne contient un chiffre (pour eviter de prendre en compte les entetes) et la date de fin du document
                    if any(char.isdigit() for char in ligne) and len(ligne) > 10:
                        info = ligne.split(' ', 4)
                        del info[2:4]
                        #Ajout de la ligne dans le tableau
                        self.tableau.append(info)
        return self.tableau

    def create_rame_list(self):
        tableau = self.extraire_donnees()
        rames = []
        for ligne in tableau:
            # Type si L -> Lapin, N -> Normal, T -> Tortue en fonction de ligne[1]
            enum_type = {
                'L': TypeEnum.Lapin,
                'N': TypeEnum.Normal,
                'T': TypeEnum.Tortue
            }.get(ligne[1], TypeEnum.Normal)
            rame = Rame(
                numero=int(ligne[0]),
                enum_type=enum_type
            )
            rames.append(rame)

        return rames

