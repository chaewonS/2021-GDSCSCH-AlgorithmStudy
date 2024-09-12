# -*- coding: utf-8 -*-
import sys
from collections import deque
read = sys.stdin.readline
# DFS
# ���ð� ��͸� ����Ѵ�.
def bfs(v):
  q = deque() # deque�� �̿��� ť ����
  q.append(v)       
  visit_list[v] = 1   
  while q:
    v = q.popleft() # ����Ǿ��ִ� ��� ���ʼ����� pop�ϸ鼭 ����
    print(v, end = " ")
    for i in range(1, n + 1):
      if visit_list[i] == 0 and graph[v][i] == 1:
        q.append(i)
        visit_list[i] = 1

def dfs(v):
  visit_list2[v] = 1        
  print(v, end = " ")
  for i in range(1, n + 1):
    if visit_list2[i] == 0 and graph[v][i] == 1:
      dfs(i)

# ������ ����n, ������ ���� m, Ž�� ���� ������ ��ȣ v
n, m, v = map(int, read().split())
# �ε��� 0���� �����ϱ� ���� n + 1
graph = [[0] * (n + 1) for _ in range(n + 1)] 
visit_list = [0] * (n + 1)
visit_list2 = [0] * (n + 1)

# ������� ���
for _ in range(m):
  a, b = map(int, read().split())
  graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)