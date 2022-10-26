import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links (=edges)
# link_list : the list ok all links between nodes
# e: the number of exit gateways
# gateways_list : the list of gateways to isole

n, l, e = [int(i) for i in input().split()]

link_list = []
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    link_list.append([n1, n2])

gateways_list = []
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateways_list.append(ei)

# Test
# print("Nb nodes : ", n, " --- nb and list of links :", l, link_list, " --- nb and list of gateways :", e, gateways_list)

# game loop ***********************************************************************************************************
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

    # create link list from de bobnet agent's position
    link_from_bobA_list = []
    for l in link_list :
            if l[0] == si :
                link_from_bobA_list.append(l)
            if l[1] == si :
                l_sorted = [l[1], l[0]]
                link_from_bobA_list.append(l_sorted)
    link_from_bobA_list = sorted(link_from_bobA_list, key=lambda x : x[1])

    #print("list of links from bobnet agent's position :", link_from_bobA_list)

    # Determine a link to cut
    link_to_cut = link_from_bobA_list[0]

    for linkbob in link_from_bobA_list :
        if linkbob[1] in gateways_list : 
            link_to_cut = linkbob

    # Instruction for the lap
    print(link_to_cut[0], link_to_cut[1])

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

