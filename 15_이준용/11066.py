from sys import stdin

rdLine = stdin.readline

t = int(rdLine())

for _ in range(t):
    k = int(rdLine())    #file 개수
    files = list(map(int, rdLine().split()))  #file들의 크기

    table = [[0]*k for _ in range(k)]

    for j in range(1, k):
        for i in range(j-1, -1, -1):
            minimum = [table[i][x] + table[x+1][j] for x in range(i, j)]
            table[i][j] = min(minimum) + sum(files[i:j+1]) #j를 포함해 더함
    print(table[0][k-1])