from sys import stdin
from collections import deque
input = stdin.readline

def bfs(f, s, visited):  
    queue = deque()
    queue.append(s)
    count = 0
    #node = ��ȣ�� ���ƴٴϴ� ��ġ
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

#f : �ǹ� �� ��
#s : ��ȣ�� ��ġ
#g : startlink�� ��ġ
#u : n��ŭ �������� �̵�
#d : n��ŭ �Ʒ������� �̵�
f,s,g,u,d = map(int, input().split())

visited = [0]*(f+1)

print(bfs(f,s,visited))