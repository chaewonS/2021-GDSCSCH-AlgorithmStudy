from sys import stdin
from collections import deque
input = stdin.readline

def bfs(knight, goal, not_visited):
    queue = deque()
    queue.append(knight)
    count = -1
    dx, dy = [-2,-1,1,2, 2,1,-1,-2],[-1,-2,-2,-1, 1,2,2,1]
    while queue:
        count += 1

        for _ in range(len(queue)):
            knight = queue.popleft()

            if not_visited[knight[0]][knight[1]]:
                not_visited[knight[0]][knight[1]] = False

                if not not_visited[knight[0]][knight[1]] and knight==goal:
                    return count

                for idx in range(8):
                    row, col = knight[0]+dx[idx], knight[1]+dy[idx]
                    if 0<=row<i and 0<=col<i and not_visited[row][col]:
                        queue.append((row, col))


t = int(input())

for _ in range(t):
    i = int(input())

    not_visited = [[True]*i for _ in range(i)]
    pos = []    #pos[0]:knight, pos[1]:goal
    for _ in range(2):
        row, col = map(int, input().split())
        pos.append((row,col))

    print(bfs(pos[0], pos[1], not_visited))