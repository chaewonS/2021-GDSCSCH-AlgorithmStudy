n = int(input())
m = 0
for m in range(n):
    num = m + sum([int(i) for i in str(m)])
    if num == n:
        print(m)
        break
if(m==n-1):
    print(0)

