from collections import deque

graph = {0: [[2, 1], [1, 1], [3, 1]], 1: [[7, 1], [0, 1], [3, 1]], 2: [[6, 1], [0, 1], [3, 1]], 3: [[7, 1], [6, 1], [5, 1], [4, 1], [0, 1], [1, 1], [2, 1]], 4: [[3, 1], [7, 1]], 5: [[3, 1], [6, 1]], 6: [[2, 1], [3, 1], [5, 1]], 7: [[3, 1], [1, 1], [4, 1]]}


def dijkstra_dist_list(graph, initial_node) :
    # ARGUMENTS FORMAT : 
    # graph : dict {'node 0' : [(node, dist), (node, dist)], 'node 1' : [(node, dist)], ...} 
    #         all keys and values are int()
    # initial_node : int() 
    
    current_node = initial_node

    current_dist = {}
    shortest_way_dict = {}
    # Mark the selected initial node with a current distance of 0 and the rest with infinity.
    for k,v in graph.items() :
        if k == current_node :
            current_dist[k] = 0
            shortest_way_dict[k] = [k]
        else :
            current_dist[k] = float('inf')
            shortest_way_dict[k] = []

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

                shortest_way_dict[n_index].extend(v for v in shortest_way_dict[current_node])
                shortest_way_dict[n_index].append(n_index)

        # Mark the current node as visited
        visited.append(current_node)

        # Chose the next node (the nearrest and non-visited from initial)    
        for k,v in current_dist.items() :
            if k not in visited and v < next_node_d : 
                next_node = k
                next_node_d = v

        """
        print("current node", current_node)
        print("visited :", visited)   
        print("next node :", next_node, next_node_d)    
        print("current_dist :", current_dist)
        """
        
        current_node = next_node

    return(current_dist, shortest_way_dict)

current_dist = dijkstra_dist_list(graph, 0)[0]
shortest_way_dict = dijkstra_dist_list(graph, 0)[1]
print("current_dist :", current_dist)
print("shortest_way_dict :", shortest_way_dict)



def dist_bet_2node(graph, a, b) :
    # ARGUMENTS FORMAT : 
    # graph : dict {'node 0' : [(node, dist), (node, dist)], 'node 1' : [(node, dist)], ...} 
    #         all keys and values are int()
    # a, b  : int(id) of two nodes 
    return(dijkstra_dist_list(graph, a)[0][b])

def path_bet_2node(graph, a, b) :
    # ARGUMENTS FORMAT : 
    # graph : dict {'node 0' : [(node, dist), (node, dist)], 'node 1' : [(node, dist)], ...} 
    #         all keys and values are int()
    # a, b  : int(id) of two nodes 
    return(dijkstra_dist_list(graph, a)[1][b])

dist = dist_bet_2node(graph, 0, 7)
path = path_bet_2node(graph, 0, 7)
print(dist)
print(path)
