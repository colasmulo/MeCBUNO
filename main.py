#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 12:33:00 2022

@author: poire
"""
import tkinter as tk
from tkinter import ttk
from planeur_ddb import Planeur_list, Planeur_list_str

Planeur_type = ["Monoplace","Biplace"]

def Calculer():#possibilite pour remplacer calculer mono : ajouter une condition dans calculer duo, où si le type de planeur est mono, forcer les valeurs de P2 à 0
    Type_sel = Type_deroul.get()
    P1 = int(Pil_av.get())
    if Type_sel == "Monoplace":
        P2 = 0
    elif Type_sel == "Biplace":
        P2 = int(Pil_ar.get())
    Planeur_input = Immat_deroul.get()
    pl_index = Planeur_list_str.index(Planeur_input)
    Masse = Planeur_list[pl_index][0] + P1 + P2
    Moment = Planeur_list[pl_index][1]*P1 + Planeur_list[pl_index][2]*P2 + Planeur_list[pl_index][3]*Planeur_list[pl_index][0]
    CG = round((Moment/Masse)*1000, 2)
    tk.Label(frame, text="Planeur : %s\nPosition du centre de gravité (en mm): %s" % (Planeur_input, CG)).grid(row=5)

# Top level window
frame = tk.Tk()
frame.title("Masse et Centrage BUNO")
#Choix type planeur
tk.Label(frame, text="Selectionnez le type de planeur :").grid(row=0)
Type_deroul = ttk.Combobox(frame, values=Planeur_type)
Type_deroul.grid(row=0, column=1)
#Immat planeur
tk.Label(frame, text="Selectionnez l'immat concours du planeur :").grid(row=1)
Immat_deroul = ttk.Combobox(frame, values=Planeur_list_str)
Immat_deroul.grid(row=1, column=1)
#Poids pil avant
tk.Label(frame, text="Masse du pilote avant en kilos :").grid(row=2)
Pil_av = tk.Entry(frame)
Pil_av.grid(row=2, column=1)
#Poids pil arriere
tk.Label(frame, text="Masse du pilote arrière en kilos (0 si  pas de pilote arrière):").grid(row=3)
Pil_ar = tk.Entry(frame)
Pil_ar.grid(row=3, column=1)

tk.Button(frame,
            text='Quitter',
            command=frame.quit).grid(row=4,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(frame,
            text='Calculer',
            command=Calculer).grid(row=4,
                                    column=1,
                                    sticky=tk.W,
                                    pady=4)
frame.mainloop()
