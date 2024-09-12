import sys
N = int(sys.stdin.readline())
sinkers = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
beads = list(map(int, sys.stdin.readline().split()))
dp = [[0]*15001 for _ in range(N + 1)]
possible = []

def dfs(sinkers, n, now, left, right):
    new = abs(left - right)
        
    if new not in possible:
        possible.append(new)
        
    if now == n : return 0
        
    if dp[now][new] == 0:
        dfs(sinkers, n, now + 1, left + sinkers[now], right) # left
        dfs(sinkers, n, now + 1, left, right + sinkers[now]) # right
        dfs(sinkers, n, now + 1, left, right) # none
        dp[now][new] = 1

dfs(sinkers, N, 0, 0, 0)
for i in range(0, M):
    if beads[i] in possible:
        print('Y', end=' ')
    else:
        print('N', end=' ')
