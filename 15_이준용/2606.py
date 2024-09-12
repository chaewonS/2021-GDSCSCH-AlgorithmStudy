from sys import stdin
from collections import deque
input = stdin.readline

queue = deque()

com_count = int(input())
connection = int(input())
computers = [[] for _ in range(com_count+1)]
infected = [False]*(com_count+1)

for _ in range(connection):
    comA, comB = map(int, input().split())
    computers[comA].append(comB)
    computers[comB].append(comA)

queue.append(1)
infected[1] = True

while queue:
    computer = queue.popleft()

    for c in computers[computer]:
        if not infected[c]:
            queue.append(c)
            infected[c] = True
        
print(infected.count(True)-1)