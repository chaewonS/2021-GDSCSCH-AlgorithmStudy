T = input()
T = int(T)

A = T // 300
T %= 300
B = T // 60
T %= 60
C = T // 10
T %= 10

if T == 0:
    print(A, B, C)
else:
    print('-1')
