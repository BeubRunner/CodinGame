import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# ENTREES
l = int(input())
h = int(input())
t = input()

# comverti list de n° de lettre [1-26] (-96 pour n° lettre / -1 pour faire correspondre A avec index 0)
tab_num_lettre = [ord(lettre) - 97 for lettre in t.lower()]

# Génère alphabet en art ASCII et les stock
tab_art = []
for i in range(h):
    row = input()
    tab_art.append(row) 

# Filtre numéro de lette
for num in range(len(tab_num_lettre)) :
    if not (0 <= tab_num_lettre[num] <= 25) :
        tab_num_lettre[num] = 26

# Genere un tab_art_cible avec les lettres à imprimer
tab_art_cible = []
for hauteur in range(h):
    ligne = ""
    for num in tab_num_lettre :
        a = num * l
        b = a + l
        ligne = ligne + f"{tab_art[hauteur][a:b]}"
    tab_art_cible.append(ligne)

# Print final
for hauteur in range(h):
    print(tab_art_cible[hauteur])
