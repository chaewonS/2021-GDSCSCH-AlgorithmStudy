import sys
n = int(input())
deq = []
for i in range(n):
    c = sys.stdin.readline().split()
    if c[0] == 'push_back':
        deq.append(c[1])

    elif c[0] == 'push_front':
        deq.insert(0, c[1])

    elif c[0] == 'pop_front':
        if len(deq) != 0:
            print(deq[0])
            del deq[0]
        else:
            print(-1)

    elif c[0] == 'pop_back':
        if len(deq) != 0:
            print(deq[-1])
            del deq[-1]
        else:
            print(-1)

    elif c[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)

    elif c[0] == 'front':
        if len(deq) != 0:
            print(deq[0])
        else:
            print(-1)

    elif c[0] == 'back':
        if len(deq) != 0:
            print(deq[-1])
        else:
            print(-1)

    elif c[0] == 'size':
        print(len(deq))