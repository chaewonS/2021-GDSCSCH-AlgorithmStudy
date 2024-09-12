import sys
n = int(sys.stdin.readline())
stack_list = []
for i in range(n):
    c = sys.stdin.readline()
    if 'push' in c:
        c, k = c.split(' ')
        k = int(k)
        stack_list.append(k)

    elif 'pop' in c:
        if len(stack_list) == 0:
            print(-1)

        else:
            print(stack_list[-1])
            del stack_list[-1]

    elif 'size' in c:
        print(len(stack_list))

    elif 'empty' in c:
        if len(stack_list) == 0:
            print(1)

        else:
            print(0)

    elif 'top' in c:
        if len(stack_list) == 0:
            print(-1)

        else:
            print(stack_list[-1])
