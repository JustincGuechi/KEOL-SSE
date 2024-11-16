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

