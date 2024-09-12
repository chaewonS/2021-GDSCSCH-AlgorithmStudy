import sys
count = int(sys.stdin.readline())
list = []

for i in range(count):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        list.insert(0, command[1])
    elif command[0] == "size":
        print(len(list))
    elif command[0] == "pop":
        if len(list) == 0:
            print(-1)
        else:
            a = list[0]
            list.pop(0)
            print(a)
    elif command[0] == "empty":
        if len(list) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if len(list) == 0:
            print(-1)
        else:
            print(list[0])