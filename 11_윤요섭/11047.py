import sys
n, k = map(int, sys.stdin.readline().split())
coin_list = []
for i in range(n):
    coin = int(sys.stdin.readline())
    coin_list.append(coin)
a = 0
for i in range(len(coin_list)):
    if k % coin_list[-(i + 1)] < k:
        a += int(k / coin_list[-(i + 1)])
        k %= coin_list[-(i + 1)]
print(a)