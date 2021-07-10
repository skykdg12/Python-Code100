graph = {'E': set(['D', 'A']),
         'F': set(['D']),
         'A': set(['A']),
         'C': set(['A']),
         'D': set(['E', 'F'])}

['E', 'A', 'B', 'C', 'D', 'F']

graph = {'E': set(['D', 'A']),
         'F': set(['D']),
         'A': set(['A']),
         'C': set(['A']),
         'D': set(['E', 'F'])}

def dfs(graph, start):
    visited = []
    stack = [start]
    
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

print(dfs(graph, 'E'))