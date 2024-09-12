from sys import stdin
input = stdin.readline
n = int(input())

houses = [[0]*3 for _ in range(n)]

for i in range(n):
    houses[i] = list(map(int,input().split()))

for i in range(1, n, 1):
    #R을 선택했을경우
    houses[i][0] += min(houses[i-1][1], houses[i-1][2])
    #G를 선택했을경우
    houses[i][1] += min(houses[i-1][0], houses[i-1][2])
    #B를 선택했을경우
    houses[i][2] += min(houses[i-1][0], houses[i-1][1])

print(min(houses[n-1]))