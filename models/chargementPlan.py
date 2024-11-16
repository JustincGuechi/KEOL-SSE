import pandas as pd
from plan import Plan
from place import Place
from enum import Enum  # Importation de la classe Enum

class Type_Place(Enum):
    RAME = 1
    RAME_IMMOBILISEE = 2
    NO_RAME = 3

def charger_excel_et_creer_plan(fichier_excel):
    # Charger le fichier Excel et lire toutes les feuilles du fichier Excel
    sheets = pd.read_excel(fichier_excel, sheet_name=None)  # sheet_name=None charge toutes les feuilles

    plans = []  # Liste pour stocker tous les plans créés

    # Parcourir chaque feuille
    for sheet_name, df in list(sheets.items())[:15]: #pour l'instant usr les 15 premiers
        # Créer un plan pour chaque feuille avec le nom de la feuille comme nom de période
        plan = Plan(nom_periode=sheet_name)

        print(str(len(plan.places)))
        print(str(len(plan.places[0])))

        for i in range(len(plan.places)):  # `i` représente l'indice de la ligne
                for j in range(len(plan.places[0])):  # `j` représente l'indice de la colonne
                    place_id = df.iloc[3+i*4, 5+j*5]
                    #if R7 crée places vides

                    #gestion des types de places
                    if place_id == "X":
                        type_place = Type_Place.NO_RAME
                    elif pd.isna(place_id):
                        type_place = Type_Place.RAME_IMMOBILISEE
                    else:
                        type_place = Type_Place.RAME
                    
                    #gestion des couleurs LNT
                    if i == 1 or i == 2:
                        couleur = "L"
                    elif i == 3 or i == 4:
                        couleur = "N"
                    elif i == 5 or i == 6:
                        couleur = "T"
                    else:
                        couleur = ""
                    

                    # Créer une instance de Place
                    place = Place(
                        ligne_id=df.iat[3+i*4, 2+j*5],
                        place_id=place_id,
                        horaire_depart=df.iat[4+i*4, 2+j*5],
                        horaire_arrivee=df.iat[4+i*4, 4+j*5],
                        horaire_depart_bis=df.iat[5+i*4, 2+j*5],
                        horaire_arrivee_bis=df.iat[5+i*4, 4+j*5],
                        type_place=type_place,
                        rame=0, #pas de rame à la lecture
                        couleur=couleur
                    )

                    # Ajouter la place à la position (i, j) dans le tableau
                    plan.ajouter_place(i, j, place)
        return plan.places



# Exemple d'utilisation
fichier_excel = "data\\20130304_SCH_DEX_Plan de remisage.xlsm"  # Nom du fichier Excel



# Charger le plan depuis l'Excel
plan = charger_excel_et_creer_plan(fichier_excel)

# Afficher le plan
print(plan)