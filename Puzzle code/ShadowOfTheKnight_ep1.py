import sys
from math import *

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

# Create a matrix h rows by w columns (using 2D list) -------------------------------------------------------------
"""
[[0, 0, 0, ..., 0]          the top left point's coordonate are (0, 0)
 [0, 0, 0, ..., 0]          X absysses goes from 0 to w-1
 [0, 0, 0, ..., 0]          Y ordinates goes from 0 to h-1
 [0, 0, 0, ..., 0]]         P(x, y) <=> list[y][x]

building = [[0 for j in range(w)] for i in range(h)]

# Shadows of the knignt = 1 into the the bulding matrix
building[y0][x0] = 1
"""
# Shadows of the knignt (x_sk, y_sk)
x_sk = x0
y_sk = y0

# Create a "search zone" list -------------------------------------------------------------------------------------
sz_list = [[0, w-1], [0, h-1]]

# tests : TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
#print(building) 
#print(sz_list) 


# *****************************************************************************************************************
# game loop *******************************************************************************************************
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Update the "search zone" list
    # Absysses
    if "R" in bomb_dir :
        sz_list[0][0] = x_sk + 1
    if "L" in bomb_dir :
        sz_list[0][1] = x_sk - 1
    # Ordonates
    if "U" in bomb_dir :
        sz_list[1][1] = y_sk - 1
    if "D" in bomb_dir :
        sz_list[1][0] = y_sk + 1
    
    #print(sz_list) 

    # Dertermine new jump coordinates
    # middle of the "search zone" ()
    x, y = 0, 0
    x = (sz_list[0][0] + sz_list[0][1]) / 2
    x = ceil(x) # ceil is nessecary to assure a min of 1
    y = (sz_list[1][0] + sz_list[1][1]) / 2
    y = ceil(y)

    # Shadows of the knignt (x_sk, y_sk) update
    x_sk = x
    y_sk = y

    # the location of the next window Batman should jump to.
    print("{} {}" .format(x, y))

    # Write an action using print
    # To debug: 
    print("Debug messages...", file=sys.stderr, flush=True)
