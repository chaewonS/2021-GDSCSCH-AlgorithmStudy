import sys
n = int(input())

nlist = []
for i in range(n):
    c = sys.stdin.readline().split()
    if c[0] == 'push':
        num = int(c[-1])
        nlist.append(num)
    elif c[0] == 'pop':
        if len(nlist) != 0:
            print(nlist[0])
            del nlist[0]
        else:
            print(-1)
    elif c[0] == 'empty':
        if len(nlist) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if len(nlist) != 0:
            print(nlist[0])
        else:
            print(-1)
    elif c[0] == 'back':
        if len(nlist) != 0:
            print(nlist[-1])
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(nlist))