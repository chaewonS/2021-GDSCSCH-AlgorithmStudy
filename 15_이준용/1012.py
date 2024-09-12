from sys import stdin
from collections import deque

input = stdin.readline

class Cavage:
    def __init__(self, col, row):
        self.col = col
        self.row = row

def bfs(farm, cavage, visited):
    dx, dy = [-1,1,0,0],[0,0,-1,1]

    queue = deque()
    queue.append(cavage)

    while queue:
        good_cvg = queue.popleft()
        if not visited[good_cvg.col][good_cvg.row]: #지렁이가 방문하지 않았다면
            visited[good_cvg.col][good_cvg.row] = 1
            for i in range(4):  #해당 배추의 상하좌우 체크, 유효한 범위 안에 있는 배추를 queue에 삽입
                col, row = dx[i]+good_cvg.col, dy[i]+good_cvg.row
                if 0<=col<n and 0<=row<m and farm[col][row]:
                    queue.append(Cavage(col, row))

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    farm = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    warm_count = 0
    for i in range(k):  #농장 표시
        row, col = map(int, input().split())
        farm[col][row] = 1
    
    for col in range(n):
        for row in range(m):
            if farm[col][row] and not visited[col][row]:
                bfs(farm, Cavage(col, row), visited)
                warm_count+=1
    print(warm_count)