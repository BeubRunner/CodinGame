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


# create targeted link list from de bobnet agent's position
targeted_link_list = []
for g in gateways_list :
    for l in link_list :
        if g in l :
            targeted_link_list.append(l)
# Test
#print("Nb nodes : ", n, " --- nb and list of gateways :", e, gateways_list, " --- targeted links :", targeted_link_list)


# Indentification of nodes linked with several gateways :
strategical_link_list = []
for n in range(n) :
    if n not in gateways_list : #for all nodes exept gateways
        tot = 0
        links = []
        for l in targeted_link_list :
            tot += l.count(n)
            if n in l :
                links.append(l)
        strategical_link_list.append([n, tot, links])
strategical_link_list = sorted(strategical_link_list, key=lambda x : x[1], reverse=True)
# Test
#print(targeted_link_list, "--------", strategical_link_list)



# game loop ***********************************************************************************************************
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

    # Determine a link to cut
    link_to_cut = [0, 0]

    """
    This methode works for only 60% of tests, 
    Breadth-first search algo is not enough, let's explorate *** Depth-first search ***

    for i in range(len(targeted_link_list)) : 
        if si in targeted_link_list[i] :                # if bob is on a node links with a gateways
            link_to_cut = targeted_link_list[i]
            break    
        else :                                          # else select a double gateways linked node 
            link_to_cut = strategical_link_list[0][2][-1]
        
    # Actualisation of  list of links
    if link_to_cut in targeted_link_list :
        targeted_link_list.pop(targeted_link_list.index(link_to_cut))
    
    if link_to_cut in strategical_link_list[0][2] :
        strategical_link_list[0][2].pop(-1)
        strategical_link_list[0][1] -= 1
        strategical_link_list = sorted(strategical_link_list, key=lambda x : x[1], reverse=True)
    # Test
    #print(link_to_cut, strategical_link_list)
    """
    # Instruction for the lap
    print(link_to_cut[0], link_to_cut[1])

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
