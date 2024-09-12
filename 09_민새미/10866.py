#덱

from collections import deque

i = int(input())
count=0
d=deque()

while(i>count):
    #print(d)
    a= input()

    if (a=="front"):
        if len(d)==0:
            print("-1")
        else :
            top = d[0]
            print(top)
    elif (a=="back"):
        if len(d)==0:
            print("-1")
        else :
            top = d[-1]
            print(top)
    elif (a=="size"):
        print(len(d))
    elif (a=="empty"):
        if(len(d)==0):
            print("1")
        else:
            print("0")
    elif (a=="pop_front"):
        if len(d)==0:
            print("-1")
        else :
            top=d.popleft()
            print(top)
    elif (a=="pop_back"):
        if len(d)==0:
            print("-1")
        else :
            top=d.pop()
            print(top)
    else:
        b, c=a.split()
        if(b=="push_front"):
            c=int(c)
            d.appendleft(c)
        elif(b=="push_back"):
            c=int(c)
            d.append(c)

    count=count+1