#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 12:33:00 2022

@author: poire
"""
import tkinter as tk

#Variables, listes
T77 = [398, -1.140, -0.011, 0.685] #[Poids à vide (kg), bras de levier pilote avant(m), bras de levier pilote arrière(mm), bras de levier CG vide]
T41 = [409, -1.140, -0.011, 0.71265]
JI = [409, -1.350, -0.270, 0.783]
LK = [412.8, -1.350, -0.270, 0.803]
PAP = [310, -5, 10, 0.7]#Valeurs par défaut à corriger
C4 = [310, -5, 10, 0.7]#Valeurs par défaut à corriger
Planeur_list = [T77, T41, JI, LK, PAP, C4]
Planeur_list_str = ["T77", "T41", "JI", "LK", "PAP", "C4"]

def Calculer():
    P1 = int(Pil_av.get())
    P2 = int(Pil_ar.get())
    Pil_tot = P1 + P2
    pl_index = Planeur_list_str.index(Planeur_input.get())
    Masse = Planeur_list[pl_index][0] + P1 + P2
    Moment = Planeur_list[pl_index][1]*P1 + Planeur_list[pl_index][2]*P2 + Planeur_list[pl_index][3]*Planeur_list[pl_index][0]
    CG = round(Moment/Masse, 4)*1000
    tk.Label(frame, text="Immat: %s\nCentre de gravité: %s" % (Planeur_input.get(), CG)).grid(row=4)
    #print("Immat: %s\nCentre de gravité: %s" % (Planeur_input.get(), CG))

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
            command=Calculer).grid(row=3,
                                    column=1,
                                    sticky=tk.W,
                                    pady=4)

frame.mainloop()