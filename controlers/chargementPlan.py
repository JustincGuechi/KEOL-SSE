import pandas as pd
from models.plan import Plan
from models.place import Place
from models.enum import Type_Place  # Importation de la classe Enum
from datetime import datetime

def extraire_heure(date_str):
        """Extrait l'heure au format hh:mm:ss d'une chaîne de caractères représentant une date/heure."""
        formats = [
            "%Y-%m-%d %H:%M:%S",  # Format '1900-01-01 01:05:00'
            "%H:%M:%S",           # Format '04:17:00'
            "%Y-%m-%d %H:%M:%S",  # Format '2024-10-30 00:00:00'
            "%H:%M"               # Format '10:05'
        ]
        
        for fmt in formats:
            try:
                dt = datetime.strptime(date_str, fmt)
                if 1 if 0 <= dt.hour < 2 else 0 :   
                    dt = dt.replace(day=2)
                    return dt.strftime("%d:%H:%M:%S")
                else:
                    dt = dt.replace(day=1)
                    return dt.strftime("%d:%H:%M:%S")
            except ValueError:
                continue
        return ""

def extraire_id(id):
    """Essaie de convertir la valeur en entier ou en chaîne de caractères,
       sinon retourne une chaîne vide."""
    
    # Tenter de convertir en entier
    try:
        return str(int(id))  # Convertir d'abord en entier, puis en chaîne
    except ValueError:
        # Si la conversion en entier échoue, tenter de convertir en chaîne directement
        try:
            return str(id)
        except Exception:
            # Si tout échoue, retourner une chaîne vide
            return ""

def charger_excel_et_creer_plan(fichier_excel):
    # Charger le fichier Excel et lire toutes les feuilles du fichier Excel
    sheets = pd.read_excel(fichier_excel, sheet_name=None)  # sheet_name=None charge toutes les feuilles

    plans = []  # Liste pour stocker tous les plans créés

    # Parcourir chaque feuille
    for sheet_name, df in list(sheets.items())[:15]: #pour l'instant usr les 15 premiers
        # Créer un plan pour chaque feuille avec le nom de la feuille comme nom de période
        plan = Plan(nom_periode=sheet_name)

        # print(str(len(plan.places)))
        # print(str(len(plan.places[0])))

        for i in range(7):  # `i` représente l'indice de la ligne
                for j in range(5):  # `j` représente l'indice de la colonne
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

                    #print("ligne", str(df.iat[3+i*4, 2+j*5]))
                    #print("horaire_depart", str(df.iat[4+i*4, 2+j*5]))
                    #print("horaire_departcv", extraire_heure(str(df.iat[4+i*4, 2+j*5])))
                    #print("horaire_arrivee", str(df.iat[4+i*4, 4+j*5]))
                    #print("heure_arriveecv", extraire_heure(str(df.iat[4+i*4, 4+j*5])))
                    # Créer une instance de Place
                    place = Place(
                        ligne_id=str(df.iat[3+i*4, 2+j*5]),
                        place_id=extraire_id(place_id),
                        horaire_depart=extraire_heure(str(df.iat[4+i*4, 2+j*5])),
                        horaire_arrivee=extraire_heure(str(df.iat[4+i*4, 4+j*5])),
                        horaire_depart_bis=extraire_heure(str(df.iat[5+i*4, 2+j*5])),
                        horaire_arrivee_bis=extraire_heure(str(df.iat[5+i*4, 4+j*5])),
                        type_place=type_place,
                        rame=0, #pas de rame à la lecture
                        couleur=couleur 
                    )
                    
                    # Ajouter la place à la position (i, j) dans le tableau
                    plan.ajouter_place(i, j, place)
        return plan
    

