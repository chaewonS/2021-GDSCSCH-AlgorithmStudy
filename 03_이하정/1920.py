n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

for k in b:
    if k in a:
        print(1)
    else:
        print(0)


