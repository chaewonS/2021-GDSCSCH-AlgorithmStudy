from sys import stdin
from collections import deque
from copy import deepcopy
input = stdin.readline

def bfs(maze, notvisited):
    node = (0, 0)
    queue = deque()
    dx, dy = [-1,1,0,0],[0,0,-1,1]
    count = 0
    queue.append(node)

    while queue:
        count+=1
        for _ in range(len(queue)):
            node = queue.popleft()
            if not_visited[node[0]][node[1]]:                
                not_visited[node[0]][node[1]] = 0
                if node[0]==n-1 and node[1]==m-1:
                    return count
                for i in range(4):
                    row, col = dx[i]+node[0], dy[i]+node[1]
                    if 0<=row<n and 0<=col<m and not_visited[row][col]:
                        queue.append((row, col))
    
n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input().rstrip())))
not_visited = deepcopy(maze)

min_count = bfs(maze, not_visited)
print(min_count)
