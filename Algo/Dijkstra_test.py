from collections import deque

graph = {0: [(2, 1), (1, 1), (3, 1)], 1: [(7, 1), (0, 1), (3, 1)], 2: [(6, 1), (0, 1), (3, 1)], 3: [(7, 1), (6, 1), (5, 1), (4, 9), (0, 1), (1, 1), (2, 1)], 4: [(3, 1), (7, 1)], 5: [(3, 1), (6, 1)], 6: [(2, 1), (3, 1), (5, 1)], 7: [(3, 1), (1, 1), (4, 1)]}


def dijkstra_dist_list(graph, initial_node) :
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

        """
        print("current node", current_node)
        print("visited :", visited)   
        print("next node :", next_node, next_node_d)    
        print("current_dist :", current_dist)
        """
        
        current_node = next_node

    return(current_dist)

current_dist = dijkstra_dist_list(graph, 0)
print("current_dist :", current_dist)