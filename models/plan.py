from place import Place
class Plan:
    def __init__(self, nom_periode):
        self.nom_periode = nom_periode  # Nom de la période
        self.places = [[None for _ in range(5)] for _ in range(7)]  # Tableau 2D de 7 voies et 5 rangements

    def ajouter_place(self, ligne, colonne, place):
        """
        Ajoute un objet Place à une position précise dans le tableau 2D.
        """
        if not isinstance(place, Place):
            raise TypeError("L'objet ajouté doit être une instance de la classe Place.")
        if ligne >= len(self.places) or colonne >= len(self.places[0]):
            raise IndexError("Les indices de ligne et colonne sont hors du tableau.")
        
        self.places[ligne][colonne] = place

    def __repr__(self):
        return f"Plan(nom_periode='{self.nom_periode}', places={self.places})"
