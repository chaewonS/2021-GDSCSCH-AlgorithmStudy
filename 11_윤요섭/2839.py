n = int(input())
l = []
for x in range(n // 3 + 1):
    for y in range(n // 5 + 1):
        if n == x * 3 + y * 5:
            l.append(x + y)
if len(l) == 0:
    print(-1)
else:
    print(min(l))