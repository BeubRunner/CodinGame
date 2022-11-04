from collections import *

graph = {0: [[2, 1], [1, 1], [3, 1]], 1: [[7, 1], [0, 1], [3, 1]], 2: [[6, 1], [0, 1], [3, 1]], 3: [[7, 1], [6, 1], [5, 1], [4, 1], [0, 1], [1, 1], [2, 1]], 4: [[3, 1], [7, 1]], 5: [[3, 1], [6, 1]], 6: [[2, 1], [3, 1], [5, 1]], 7: [[3, 1], [1, 1], [4, 1]]}

def iterative_bfs(graph, node):
    visited = []

    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            unvisited = []
            for n in graph[node] :
                if n[0] not in visited :
                    unvisited.append(n[0])
            queue.extend(unvisited)

    return(visited)

v = iterative_bfs(graph, 0)
print(v)