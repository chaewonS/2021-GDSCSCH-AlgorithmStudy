from sys import stdin

input = stdin.readline

n, m ,v = map(int, input().split())

visited=[False] * (n+1)
graph = [[] for _ in range(n+1)]
stack = []

for _ in range(m):
    nodeA, nodeB = map(int, input().split())
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)
    graph[nodeA].sort()
    graph[nodeB].sort()

# [nodeA] : [nodeB1, nodeB2, ...]
def dfs_recursive(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for node in graph[v]:
        if not visited[node]:
            dfs_recursive(graph, node, visited)
def dfs_iterative(graph, v, visited):
    stack = [v]

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')
            stack.extend(reversed(graph[v]))

def bfs(graph, v, visited):
    queue = [v]    
    visited[v] = True
    print(v, end=' ')

    while queue:
        v = queue.pop(0)
        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                print(node, end=' ')
        
dfs_iterative(graph, v, visited.copy())
print()
bfs(graph, v, visited.copy())
