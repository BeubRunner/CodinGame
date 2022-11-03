from collections import *

def iterative_dfs(graph, node):
    visited = []
    stack = deque()
    stack.append(node)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            unvisited = [n for n in graph[node] if n not in visited]
            stack.extend(unvisited)

    return visited