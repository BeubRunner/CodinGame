graph = {0: [[10, 1], [1, 1], [6, 1], [9, 1], [11, 1], [7, 1]], 1: [[0, 1], [2, 1], [4, 1], [6, 1], [7, 1], [3, 1]], 2: [[5, 1], [35, 1], [1, 1], [3, 1], [4, 1], [34, 1], [33, 1]], 3: [[8, 1], [33, 1], [2, 1], [19, 1], [20, 1], [1, 1]], 4: [[1, 1], [5, 1], [2, 1], [6, 1]], 5: [[2, 1], [35, 1], [4, 1]], 6: [[1, 1], [4, 1], [11, 1], [12, 1], [0, 1]], 7: [[13, 1], [1, 1], [9, 1], [0, 1], [36, 1]], 8: [[16, 1], [3, 1], [17, 1], [19, 1], [36, 1]], 9: [[14, 1], [13, 1], [10, 1], [7, 1], [0, 1]], 10: [[0, 1], [11, 1], [9, 1], [14, 1]], 11: [[12, 1], [10, 1], [6, 1], [0, 1]], 12: [[11, 1], [6, 1]], 13: [[14, 1], [16, 1], [7, 1], [15, 1], [9, 1], [36, 1]], 14: [[13, 1], [9, 1], [15, 1], [10, 1]], 15: [[13, 1], [14, 1], [24, 1], [16, 1], [23, 1]], 16: [[13, 1], [8, 1], [23, 1], [17, 1], [27, 1], [30, 1], [15, 1]], 17: [[31, 1], [16, 1], [18, 1], [8, 1], [32, 1], [19, 1]], 18: [[17, 1], [32, 1], [22, 1], [19, 1]], 19: [[21, 1], [22, 1], [20, 1], [3, 1], [17, 1], [18, 1], [8, 1]], 20: [[19, 1], [3, 1], [21, 1]], 21: [[19, 1], [20, 1], [32, 1], [22, 1]], 22: [[19, 1], [32, 1], [18, 1], [21, 1]], 23: [[16, 1], [24, 1], [25, 1], [27, 1], [15, 1]], 24: [[23, 1], [25, 1], [15, 1]], 25: [[26, 1], [23, 1], [24, 1], [27, 1]], 26: [[28, 1], [25, 1], [27, 1]], 27: [[16, 1], [26, 1], [25, 1], [29, 1], [30, 1], [23, 1], [28, 1]], 28: [[26, 1], [29, 1], [27, 1]], 29: [[30, 1], [28, 1], [27, 1]], 30: [[29, 1], [16, 1], [27, 1]], 31: [[17, 1], [32, 1]], 32: [[22, 1], [18, 1], [31, 1], [17, 1], [21, 1]], 33: [[34, 1], [3, 1], [2, 1]], 34: [[35, 1], [33, 1], [2, 1]], 35: [[5, 1], [2, 1], [34, 1]], 36: [[7, 1], [13, 1], [8, 1]]}

gateways_list = [0, 16, 18, 26]
si = 3

def dijkstra_dist_list(graph, initial_node) : # return a dict of shortest dist from initial node to each others
    # ARGUMENTS FORMAT : 
    # graph : dict {'node 0' : [(node, dist), (node, dist)], 'node 1' : [(node, dist)], ...} 
    #         all keys and values are int()
    # initial_node : int() 


    current_node = initial_node
    # Mark the selected initial node with a current distance of 0 and the rest with infinity.
    current_dist = {}
    for k,v in graph.items() :
        if k == current_node :
            current_dist[k] = 0
        else :
            current_dist[k] = float('inf')

    visited = []
    while len(visited) != len(graph.keys()) :
        queue = deque()
        next_node, next_node_d = current_node, float('inf')

        # Visit the direct neighbours of the current node and add distances into current distances list 
        for v in graph[current_node] :
            queue.append(v)

        while queue :
            node = queue.popleft()
            n_index, n_dist = node[0], node[1]
            if current_dist[current_node] + n_dist < current_dist[n_index] :
                current_dist[n_index] = current_dist[current_node] + n_dist

        # Mark the current node as visited
        visited.append(current_node)

        # Chose the next node (the nearrest and non-visited from initial)    
        for k,v in current_dist.items() :
            if k not in visited and v < next_node_d : 
                next_node = k
                next_node_d = v

        current_node = next_node

    return(current_dist)

def dist_bet_2node(graph, a, b) :   # return integer distance bet. 2 nodes a, b
    # ARGUMENTS FORMAT : 
    # graph : dict {'node 0' : [(node, dist), (node, dist)], 'node 1' : [(node, dist)], ...} 
    #         all keys and values are int()
    # a, b  : int(id) of two nodes 
    return(dijkstra_dist_list(graph, a)[b])

def update_cuted_link(graph, a, b) : # set a dist = infiny bet. 2 nodes a, b 
    # ARGUMENTS FORMAT : 
    # graph : dict {'node 0' : [(node, dist), (node, dist)], 'node 1' : [(node, dist)], ...} 
    #         all keys and values are int()
    for v in graph[a] : 
        if v[0] == b : 
            v[1] = float('inf')
    for v in graph[b] : 
        if v[0] ==  a : 
            v[1] = float('inf') 
    return(graph)

def gateways_count(graph, gateways_list) :
    gateways_connected = {}
    for k in graph : 
        gateways_connected[k] = []
    for k,v in graph.items():
        for n in v :
            if n[0] in gateways_list :
                gateways_connected[k].append(n[0])

    filtre_empty = {k:v for k,v in gateways_connected.items() if len(v) > 0}
    gateways_connected = filtre_empty

    return(gateways_connected)

target_node_dict = gateways_count(graph, gateways_list)
print(target_node_dict)

gateways_dict = {}
for n in gateways_list : 
    gateways_dict[n] = len(graph[n])
print(gateways_dict)

print(len(target_node_dict[17]))


