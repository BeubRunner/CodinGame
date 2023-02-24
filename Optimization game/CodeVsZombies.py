import sys
from  math import *

# Save humans, destroy zombies!

def dist(h, z) :
    #h = [human_id, human_x, human_y]
    #z = [zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext]
    dist = sqrt((z[3] - h[1])**2 + (z[4] - h[2])**2)
    return(dist)



# game loop ******************************************************************************************************
while True:
    x, y = [int(i) for i in input().split()]
    human_count = int(input())

    human_list = []
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        human_list.append([human_id, human_x, human_y])
    
    zombie_count = int(input())
    zombie_list = []
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        zombie_list.append([zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext])

    # Test : 
    print("Ash :", x, y, "--- humain :", human_count, human_list, "--- zombie :", zombie_count, zombie_list)

    # Distance human / zombie
    dist_hz_list = [] #[human_id, zombie_id, distance]
    for h in human_list:
        for z in zombie_list:
            d = dist(h, z)
            dist_hz_list.append([h[0], z[0], d])
    
    # Test : 
    #print("distances :", dist_list)

    
    # Coordinate of the human with nearrest danger
    # memo human_list format : [[human_id, human_x, human_y, human_ergency_ind]]
    dist_min = min(dist_hz_list, key=lambda x : x[3])


    """
    # Emergency indice for each human
    # inversely proportional to the square of the sum of distances
    for h in human_list:
        s = 0
        for d in dist_hz_list :
            if d[0] == h[0] :
                s += d[2]
        emergency_ind = floor(1E+12/s**2)
        h.append(emergency_ind)

    # Test : 
    #print("human_list with distances :", human_list)
    """

    """
    # Human centroid coordinate
    # memo human_list format : [[human_id, human_x, human_y, human_ergency_ind]]
    human_centroid = [0, 0]
    human_centroid[0] = floor(sum(e[1]*e[3] for e in human_list) / sum(e[3] for e in human_list))
    human_centroid[1] = floor(sum(e[2]*e[3] for e in human_list) / sum(e[3] for e in human_list))

    # Test : 
    #print(human_centroid)
    """

    # Ash's next destination
    Ash_next = [0, 0]
    Ash_next = [dist_min[1], dist_min[2]]

    # Final Instruction IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
    print(Ash_next[0], Ash_next[1])

    # Test : 
    #print("Ash :", x, y, "--- humain centroid :", human_count, human_list, human_centroid, "--- zombie_next centroid :", zombie_count, zombie_list, zombie_next_centroid)


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Your destination coordinates
    #print("0 0")
