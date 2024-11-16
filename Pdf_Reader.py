#Ce fichier sera utiliser pour l'extraction des données d'un pdf

import pdfplumber

# Ouvrir le fichier PDF
chemin_du_pdf = 'Données sources KDM/KM_parcourus_S44-2024.pdf'

#Tableau des données extraites du PDF (format : [Num_ram,Type,Remaque])
tableau = []
position = 0
# Lire le contenu du PDF
with pdfplumber.open(chemin_du_pdf) as pdf:
    for num_page, page in enumerate(pdf.pages):
        texte = page.extract_text()
        lignes = texte.split('\n')
        for ligne in lignes:
            # Si la ligne contient un chiffre (pour eviter de prendre en compte les entetes) et la date de fin du document
            if any(char.isdigit() for char in ligne) and len(ligne) > 10:
                #print(ligne)
                info = ligne.split(' ', 4)
                del info[2:4]
                #Ajout de la ligne dans le tableau
                tableau.append(info)
                
print(tableau)