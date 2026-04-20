import customtkinter as ctk
from services.services_salle import ServiceSalle
from models.salle import Salle
from tkinter import ttk
class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.service = ServiceSalle()
        self.title("Room management")
        self.geometry("500x500")
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
        self.btn_search = ctk.CTkButton(self.cadreButtons, text="Rechercher", command=self.rechercher_salle)
        self.btn_search.grid(row=0, column=3, padx=5)