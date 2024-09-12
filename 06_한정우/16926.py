import sys

n, m, r = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m) // 2):
        x, y = i, i
        next_value = array[x][y]

        for j in range(i + 1, n - i):
            x = j
            prev_value = array[x][y]
            array[x][y] = next_value
            next_value = prev_value

        for j in range(i + 1, m - i):
            y = j
            prev_value = array[x][y]
            array[x][y] = next_value
            next_value = prev_value
            
        for j in range(i + 1, n - i):
            x = n - j - 1
            prev_value = array[x][y]
            array[x][y] = next_value
            next_value = prev_value

        for j in range(i + 1, m - i):
            y = m - j -1
            prev_value = array[x][y]
            array[x][y] = next_value
            next_value = prev_value

for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print()
