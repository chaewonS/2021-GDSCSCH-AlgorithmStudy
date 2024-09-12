from sys import stdin
from collections import deque

input = stdin.readline

def bfs(graph, node, visited):
    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = True
            for conNode in graph[node]:
                queue.append(conNode)

n, m = map(int, input().split())

graph = [[]for i in range(n+1)]
visited = [False]*(n+1)
conComp = 0

for i in range(1,m,1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for node in range(1,n,1):
    if not visited[node]:
        bfs(graph, node, visited)
        conComp += 1
print(conComp)