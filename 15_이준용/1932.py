from sys import stdin

input = stdin.readline

n = int(input())

triang = [[0] for i in range(n)]
for i in range(n):
    triang[i] = list(map(int, input().split()))

# left node : list[i][j] += list[i-1][j]
# right node : list[i][j] += list[i-1][j-1]
# list[i][0], list[i][end]는 각각 right와 left node가 없으므로 예외
for i in range(1,n,1):
    for j in range(len(triang[i])):
        if j == 0:
            triang[i][j] += triang[i-1][j]
        elif j == len(triang[i])-1:
            triang[i][j] += triang[i-1][j-1]
        else:
            triang[i][j] += max(triang[i-1][j],triang[i-1][j-1])

print(max(triang[n-1]))