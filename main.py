#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 12:33:00 2022

@author: poire
"""
import tkinter as tk

def show_entry_fields():
    Pil_tot = str(int(Pil_av) + int(Pil_ar))
    print("Immat: %s\nMasse pilotes totale: %s" % (Planeur_input.get(), Pil_tot.get()))

T77 = [398, -1.140, -0.011, 0.685] #[Poids à vide (kg), bras de levier pilote avant(m), bras de levier pilote arrière(mm), bras de levier CG vide]
T41 = [409, -1.140, -0.011, 0.71265]
JI = [409, -1.350, -0.270, 0.783]
LK = [412.8, -1.350, -0.270, 0.803]
PAP = [310, -5, 10]
C4 = [310, -5, 10]
Planeur_list = [T77, T41, JI, LK, PAP, C4]
Planeur_list_str = ["T77", "T41", "JI", "LK", "PAP", "C4"]

# Top level window
frame = tk.Tk()
frame.title("Masse et Centrage BUNO")
frame.config(bg = 'gray50')
#frame.geometry('400x200')
#Immat planeur
tk.Label(frame, text="Entrez l'immat concours du planeur :").grid(row=0)
Planeur_input = tk.Entry(frame)
Planeur_input.grid(row=0, column=1)
#Poids pil avant
tk.Label(frame, text="Masse du pilote avant en kilos :").grid(row=1)
Pil_av = tk.Entry(frame)
Pil_av.grid(row=1, column=1)
#Poids pil arriere
tk.Label(frame, text="Masse du pilote arrière en kilos (0 si  pas de pilote arrière):").grid(row=2)
Pil_ar = tk.Entry(frame)
Pil_ar.grid(row=2, column=1)

tk.Button(frame,
            text='Quitter',
            command=frame.quit).grid(row=3,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(frame,
            text='Calculer',
            command=show_entry_fields).grid(row=3,
                                    column=1,
                                    sticky=tk.W,
                                    pady=4)

frame.mainloop()
#("Entrez l'immat concours du planeur :")

#Pil_av = int(input ("Masse du pilote avant en kilos :"))
#Pil_ar = int(input ("Masse du pilote arrière en kilos (0 si  pas de pilote arrière):"))
#pl_index = Planeur_list_str.index(Planeur_input)
#Masse = Planeur_list[pl_index][0] + Pil_av + Pil_ar
#Moment = Planeur_list[pl_index][1]*Pil_av + Planeur_list[pl_index][2]*Pil_ar + Planeur_list[pl_index][3]*Planeur_list[pl_index][0]
#CG = round(Moment/Masse, 4)*1000
#print("Centre de gravité en mm:", CG)
