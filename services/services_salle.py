from Data.dao_salle import DataSalle

class ServiceSalle:
    def __init__(self):
        self.dao = DataSalle()

    def ajouter_salle(self, salle):
        if not all([salle.code, salle.description, salle.categorie, salle.capacite]):
            return False, "All fields are required."
        if salle.capacite < 1:
            return False, "invalid capacity"

        self.dao.insert_salle(salle)
        return True, "Salle add"