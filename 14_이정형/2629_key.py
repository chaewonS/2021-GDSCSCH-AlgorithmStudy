import sys

n = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

possible = {0: True}
for i in c:
    add = []
    for j in possible.keys():
        add.append(abs(i - j))
        add.append(abs(i + j))
    for j in add:
        possible[j] = True
answer = ""
for i in b:
    if i in possible:
        answer = answer + "Y "
    else:
        answer = answer + "N "
print(answer[:-1])
