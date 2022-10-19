import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

liste = []
liste_abs = []

n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    liste.append(t)
    liste_abs.append(abs(t))

if len(liste) == 0 :
    print("0")
    exit()

ind = liste_abs.index(min(liste_abs))
valeur_mini = liste[ind]
if abs(valeur_mini) in liste : 
    valeur_mini = abs(valeur_mini)

print(valeur_mini)
