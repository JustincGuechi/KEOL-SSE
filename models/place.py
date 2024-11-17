
class Place:
    def __init__(self, ligne_id, place_id, horaire_depart, horaire_arrivee,horaire_depart_bis, horaire_arrivee_bis, type_place, rame, couleur):
        self.ligne_id = ligne_id  # Identifiant de ligne (T1, T2, 91, 92)
        self.place_id = place_id  # Identifiant unique de la place
        self.horaire_depart = horaire_depart  # Horaire de départ
        self.horaire_depart_bis = horaire_depart_bis  # Horaire de départ
        self.horaire_arrivee = horaire_arrivee  # Horaire d'arrivée
        self.horaire_arrivee_bis = horaire_arrivee_bis  # Horaire d'arrivée
        self.type_place = type_place  # IMO
        self.rame = rame  # Rame associée
        self.couleur = couleur  # Type (Lapin, Tortue)

    def __repr__(self):
        return (f"Place(ligne_id='{self.ligne_id}', place_id='{self.place_id}', "
                f"horaire_depart='{self.horaire_depart}', horaire_arrivee='{self.horaire_arrivee}', "
                f"type_place='{self.type_place}', rame='{self.rame}', couleur='{self.couleur}')")
    
    
    def to_dict(self):
        """Convertir l'objet Place en un dictionnaire sérialisable en JSON"""
        return {
            'ligne_id': self.ligne_id,
            'place_id': self.place_id,
            'horaire_depart': self.horaire_depart,
            'horaire_depart_bis': self.horaire_depart_bis,
            'horaire_arrivee': self.horaire_arrivee,
            'horaire_arrivee_bis': self.horaire_arrivee_bis,
            'type_place': self.type_place.name,
            'rame': self.rame,
            'couleur': self.couleur
        }

    '''def time_to_string(self, time_obj):
        """Convertit un objet time en une chaîne de caractères formatée"""
        if isinstance(time_obj, time):  # Vérifie si l'objet est bien de type time
            return time_obj.strftime('%H:%M')  # Exemple: '08:30'
        return str(time_obj)  # Si ce n'est pas un objet time, on le convertit en chaîne directement'''


