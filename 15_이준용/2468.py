from sys import stdin
from collections import deque
from copy import deepcopy
input = stdin.readline

n = int(input())

def bfs(land, col, row, not_visited, rain):
    dx, dy = [-1,1,0,0],[0,0,-1,1]
    queue = deque()
    queue.append((col, row))
    while queue:
        node = queue.popleft()
        if not_visited[node[0]][node[1]]:
            not_visited[node[0]][node[1]] = 0
            for i in range(4):
                col, row = node[0]+dx[i], node[1]+dy[i]
                if 0<=col<n and 0<=row<n and land[col][row]>rain:
                    queue.append((col,row))

land = []
max_height = 0
for _ in range(n):
    line = list(map(int, input().split()))
    land.append(line)
    max_height =max(max_height, max(line))

safety_area = [0]*(max_height+1)

for rain in range(0, max_height,1):
    not_visited =  deepcopy(land)  #0이면 방문, 다른 정수면 방문X
    for col in range(n):
        for row in range(n):
            if (land[col][row]>rain) and (not_visited[col][row]):
                bfs(land, col, row, not_visited, rain)
                safety_area[rain] += 1

print(max(safety_area))