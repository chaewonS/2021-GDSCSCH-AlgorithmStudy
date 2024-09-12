from sys import stdin

input = stdin.readline

def dp(n, num):
    count = 0
    if n == num:
        return 1
    elif n < num:
        return 0

    count += dp(n, num+1)
    count += dp(n, num+2)
    count += dp(n, num+3)
    return count

t = int(input())

for _ in range(t):
    n = int(input())

    count = dp(n, 0)
    print(count)