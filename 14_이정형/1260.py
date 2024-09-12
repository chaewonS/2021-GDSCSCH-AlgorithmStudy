# -*- coding: utf-8 -*-
import sys
from collections import deque
read = sys.stdin.readline
# DFS
# 스택과 재귀를 사용한다.
def bfs(v):
  q = deque() # deque를 이용한 큐 생성
  q.append(v)       
  visit_list[v] = 1   
  while q:
    v = q.popleft() # 저장되어있는 노드 왼쪽서부터 pop하면서 진행
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

# 정점의 개수n, 간선의 개수 m, 탐색 시작 정점의 번호 v
n, m, v = map(int, read().split())
# 인덱스 0부터 시작하기 위해 n + 1
graph = [[0] * (n + 1) for _ in range(n + 1)] 
visit_list = [0] * (n + 1)
visit_list2 = [0] * (n + 1)

# 인접행렬 사용
for _ in range(m):
  a, b = map(int, read().split())
  graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)