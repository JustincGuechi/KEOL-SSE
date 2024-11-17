import json
import pandas as pd
import shutil


class Json_to_Excel:
    def __init__(self, path, jsons):
        self.path = path
        self.json = json.loads(jsons)
        


    def json_to_excel(self):
        """Convertit les données JSON en un fichier Excel."""
        # Créer une copie du fichier Excel existant
        backup_path = self.path.replace('.xlsm', '_backup.xlsm')
        shutil.copyfile(self.path, backup_path)
        # Vérifier si le JSON contient les clés nécessaires
        if 'places' not in self.json or 'maintenances' not in self.json:
            raise ValueError("Le JSON doit contenir les clés 'places' et 'maintenances'")

        print(type(self.json))
        
        # Récupérer les données de chaque clé
        nom_periode = self.json['nom_periode']
        places_data = self.json['places']
        maintenances_data = self.json['maintenances']

        # Charger le fichier Excel existant
        try:
            existing_excel = pd.ExcelFile(backup_path, engine='openpyxl')
        except FileNotFoundError:
            existing_excel = None

        # Créer un writer Excel avec le fichier existant ou un nouveau fichier
        writer = pd.ExcelWriter(backup_path, engine='openpyxl')

        if existing_excel:
            # Copier uniquement la feuille dont le nom est nom_periode dans le writer
            if nom_periode in existing_excel.sheet_names:
                existing_df = pd.read_excel(backup_path, sheet_name=nom_periode, engine='openpyxl')
                existing_df.to_excel(writer, sheet_name=nom_periode, index=False)
            else:
                raise ValueError(f"La feuille nommée {nom_periode} n'existe pas dans le fichier Excel.")


        for i in range(7):  # `i` représente l'indice de la ligne
            for j in range(5):  # `j` représente l'indice de la colonne
                id_ligne = existing_df.iat[3+i*4, 2+j*5]
                if id_ligne != "X":
                    for place in places_data:
                        if place['ligne_id'] == id_ligne:
                            existing_df.iat[3+i*4, 3+j*5] = place['rame']
                            break

        
        # Sauvegarder le fichier Excel
        writer.save()
        return backup_path