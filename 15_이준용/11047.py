from sys import stdin

n, k = map(int, stdin.readline().split())
coins = []
coin_count = 0

for _ in range(n):
    coins.append(int(stdin.readline()))

coins.reverse()
for coin in coins:
    if k >= coin:
        count, k = divmod(k,coin)
        coin_count += count
print(coin_count)