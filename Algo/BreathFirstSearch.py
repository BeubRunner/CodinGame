# Breath First Search algo
from collections import *

def iterative_bfs(graph, node):
    visited = []
    line = deque()
    line.append(node)

    while queue:
        node = line.popleft()
        if node not in visited:
            visited.append(node)
            unvisited = [n for n in graph[node] if n not in visited]
            line.extend(unvisited)

    return visited