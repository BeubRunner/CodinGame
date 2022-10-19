import sys
import math
import binascii

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
# conversion en entier Unicode puis en en binaire en assemblage avec espace
"""
mess_bin = "".join(format(ord(lettre), "07b") for lettre in message)
print(mess_bin)
"""
mess_bin = ''.join(format(x, '07b') for x in bytearray(message, 'utf-7'))
#print(mess_bin)

# Def de la fonction d'encriptage d'une string binaire
def encripte(str_bin) :
    # Déclaration variables
    list_count = []
    str_bin_encr = ""
    bit_value = ""
    bit_value_prev = ""
    bit_value_encr = ""
    compteur = ""

    # conversion en list   
    for letter in str_bin : 
        list_count.append(letter)   

    # encriptage list
    for e in range(len(list_count)) : # pour chaque index de la list 
        
        bit_value = list_count[e]

        # Traitement 1er caractère
        if e == 0 : 
            compteur = "0"

            if bit_value == "0" :
                bit_value_encr = "00"
            else :
                bit_value_encr = "0"

            bit_value_prev = bit_value
            
        # Traitement des caractères suivants
        else : 
            if bit_value == bit_value_prev :
                compteur = compteur + "0"
            else :
                str_bin_encr = str_bin_encr + bit_value_encr + " " + compteur
                compteur = "0"
                if bit_value == "0" :
                    bit_value_encr = " 00"
                else :
                    bit_value_encr = " 0"

            bit_value_prev = bit_value
        
        # Sortie pour dernière itération
        if e == len(list_count) - 1 :
            str_bin_encr = str_bin_encr + bit_value_encr + " " + compteur          

    return(str_bin_encr)

print(encripte(mess_bin))   