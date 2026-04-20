import customtkinter as ctk
from services.services_salle import ServiceSalle
from models.salle import Salle
from tkinter import ttk
from tkinter import messagebox
class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.service = ServiceSalle()
        self.title("Room management")
        self.geometry("700x400")
        self.cadreInfo = ctk.CTkFrame(self)
        self.cadreInfo.pack(pady=10, padx=10)
        ctk.CTkLabel(self.cadreInfo, text="Code").grid(row=0, column=0)
        self.entry_code = ctk.CTkEntry(self.cadreInfo)
        self.entry_code.grid(row=0, column=1)
        ctk.CTkLabel(self.cadreInfo, text="Description").grid(row=1, column=0)
        self.entry_description = ctk.CTkEntry(self.cadreInfo)
        self.entry_description.grid(row=1, column=1)
        ctk.CTkLabel(self.cadreInfo, text="Catégorie").grid(row=2, column=0)
        self.entry_categorie = ctk.CTkEntry(self.cadreInfo)
        self.entry_categorie.grid(row=2, column=1)
        ctk.CTkLabel(self.cadreInfo, text="Capacité").grid(row=3, column=0)
        self.entry_capacite = ctk.CTkEntry(self.cadreInfo)
        self.entry_capacite.grid(row=3, column=1)
        self.cadreButtons = ctk.CTkFrame(self)
        self.cadreButtons.pack(pady=10)
        self.btn_add = ctk.CTkButton(self.cadreButtons, text="Ajouter", command=self.ajouter_salle)
        self.btn_add.grid(row=0, column=0, padx=5)
        self.btn_delete = ctk.CTkButton(self.cadreButtons, text="Supprimer", command=self.supprimer_salle)
        self.btn_delete.grid(row=0, column=2, padx=5)
        self.btn_update = ctk.CTkButton(self.cadreButtons, text="Modifier", command=self.modifier_salle)
        self.btn_update.grid(row=0, column=1, padx=5)
        self.btn_search = ctk.CTkButton(self.cadreButtons, text="Rechercher", command=self.rechercher_salle)
        self.btn_search.grid(row=0, column=3, padx=5)
        self.cadreList = ctk.CTkFrame(self)
        self.cadreList.pack(pady=10, padx=10)
######################################
        self.treeList = ttk.Treeview(
            self.cadreList,
            columns=("code", "description", "categorie", "capacite"),
            show="headings"
        )
        self.treeList.heading("code", text="CODE")
        self.treeList.heading("description", text="Description")
        self.treeList.heading("categorie", text="Catégorie")
        self.treeList.heading("capacite", text="Capacité")
        self.treeList.pack(expand=True, fill="both")
        self.lister_salles()

    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())

        liste = self.service.recuperer_salles()

        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.description, s.categorie, s.capacite))


    def ajouter_salle(self):
        code = self.entry_code.get()
        description = self.entry_description.get()
        categorie = self.entry_categorie.get()
        capacite = self.entry_capacite.get()
        print(code, description, categorie, capacite)
        try:
            capacite = int(capacite)
        except:
            print("Capacité invalide")
            return

        salle = Salle(code, description, categorie, capacite)

        success, message = self.service.ajouter_salle(salle)

        print(message)
        self.lister_salles()
    def supprimer_salle(self):
        code = self.entry_code.get()
        self.service.supprimer_salle(code)
        print("Salle supprimée")
        self.lister_salles()
    def rechercher_salle(self):
        code = self.entry_code.get()

        salle = self.service.rechercher_salle(code)

        if salle:
            self.entry_description.delete(0, 'end')
            self.entry_categorie.delete(0, 'end')
            self.entry_capacite.delete(0, 'end')

            self.entry_description.insert(0, salle.description)
            self.entry_categorie.insert(0, salle.categorie)
            self.entry_capacite.insert(0, salle.capacite)
        else:
            print("Salle non trouvée")
            self.lister_salles()

    def modifier_salle(self):
        print("clicked modifier")

        code = self.entry_code.get()
        description = self.entry_description.get()
        categorie = self.entry_categorie.get()
        capacite = self.entry_capacite.get()

        print(code, description, categorie, capacite)

        try:
            capacite = int(capacite)
        except:
            print("Capacité invalide")
            return

        salle = Salle(code, description, categorie, capacite)

        success, message = self.service.modifier_salle(salle)

        print("Salle Modifee")
        self.lister_salles()




