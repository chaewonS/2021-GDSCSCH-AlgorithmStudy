from sys import stdin
from collections import deque
input = stdin.readline

m, n = map(int, input().split())

class Node:
    def __init__(self, col, row):
        self.col = col
        self.row = row

box = []
visited = [[0]*m for j in range(n)]
queue = deque()
dx, dy = [-1,1,0,0],[0,0,-1,1]

for idx in range(n):
    temp = list(map(int, input().split()))
    box.append(temp)

    for i in range(m):
        if temp[i] == 1:
            queue.append(Node(idx, i))  #큐에 초기 익은 토마토 추가
        elif temp[i] == -1:
            visited[idx][i] = -1  #빈칸도 미리 표시

counter=-1
while queue:
    for _ in range(len(queue)):
        redTMT = queue.popleft()
        if visited[redTMT.col][redTMT.row] == 0:
            visited[redTMT.col][redTMT.row] = 1

            for i in range(4):
                col, row = dx[i]+redTMT.col, dy[i]+redTMT.row

                if 0<=col<n and 0<=row<m and box[col][row]==0:
                    box[col][row] = 1
                    queue.append(Node(col,row))
    counter+=1
    
for line in box:
    if 0 in line:
        counter=-1
        break
print(counter)

for i in box:
    print(i)
print()
for j in visited:
    print(j)