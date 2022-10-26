import sys
import math
from collections import *

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways

n, l, e = [int(i) for i in input().split()]

link_dict = {}
for i in range(n) :
    link_dict[i] = []

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    link_dict[n1].append(n2)
    link_dict[n2].append(n1)
#print(link_dict)

# Gateways list
gateways_list = []
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateways_list.append(ei)

# Breath First Search algo
def iterative_bfs(graph, start) : 
    # graph : a graph within a dict() format
    # start : the node to start
    visited = []
    line = deque()
    line.append(start)
    while line :
        node = line.popleft()
        if node not in visited :
            visited.append(node)
            unvisited = [n for n in graph[node] if n not in visited]
            line.extend(unvisited)           
        for j in unvisited : 
            if j in gateways_list :
                gate = j
                return(node, gate)
    return(node)

# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

    first_exit_found = iterative_bfs(link_dict, si)

    print(first_exit_found[0], first_exit_found[1])




