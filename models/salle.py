class salle :
    def __init__(self,code , decr , categorie , capacite) :
        self.code = code
        self.description = decr
        self.categorie = categorie
        self.capacite = capacite

    def afficher_info(self ):
         return f"code: {self.code}, description: {self.desc}, catégorie: {self.categorie}, capacité: {self.capacite}"
