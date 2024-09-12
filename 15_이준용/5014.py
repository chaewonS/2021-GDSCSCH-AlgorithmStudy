from sys import stdin
from collections import deque
input = stdin.readline

def bfs(f, s, visited):  
    queue = deque()
    queue.append(s)
    count = 0
    #node = 강호가 돌아다니는 위치
    while queue:
        count += 1

        for _ in range(len(queue)):
            node = queue.popleft()

            if not visited[node]:
                visited[node] = count

                if node == g and visited[node]:
                    return visited[node]-1

                if 0<node-d:
                    queue.append(node-d)
                if node+u<=f:
                    queue.append(node+u)

    return 'use the stairs'

#f : 건물 층 수
#s : 강호의 위치
#g : startlink의 위치
#u : n만큼 윗층으로 이동
#d : n만큼 아래층으로 이동
f,s,g,u,d = map(int, input().split())

visited = [0]*(f+1)

print(bfs(f,s,visited))