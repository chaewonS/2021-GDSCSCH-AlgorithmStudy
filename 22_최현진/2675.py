T = int(input())

for i in range(T):
    R, S = map(str, input().split())
    R = int(R)
    for j in S:
        k = 0
        for k in range(R):
            print(j, end='')
    print()