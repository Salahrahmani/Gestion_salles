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