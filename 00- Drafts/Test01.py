graph = {0: [[2, 1], [1, 1], [3, 1]], 1: [[7, 1], [0, 1], [3, 1]], 2: [[6, 1], [0, 1], [3, 1]], 3: [[7, 1], [6, 1], [5, 1], [4, 1], [0, 1], [1, 1], [2, 1]], 4: [[3, 1], [7, 1]], 5: [[3, 1], [6, 1]], 6: [[2, 1], [3, 1], [5, 1]], 7: [[3, 1], [1, 1], [4, 1]]}

print(graph)

def update_cuted_link(graph, a, b) : # set a dist = infiny bet. 2 nodes a, b 
    # ARGUMENTS FORMAT : 
    # graph : dict {'node 0' : [(node, dist), (node, dist)], 'node 1' : [(node, dist)], ...} 
    #         all keys and values are int()
    for v in graph[a] : 
        if v[0] == b :
            graph[a].remove(v)
    for v in graph[b] : 
        if v[0] ==  a : 
            graph[b].remove(v)
    return(graph)

graph = update_cuted_link(graph, 3, 4)
print(graph)