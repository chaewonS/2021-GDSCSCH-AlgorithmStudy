#큐

import queue

i = int(input())
count=0
queue=[]

while(i>count):

    a= input()

    if (a=="front"):
        if len(queue)==0:
            print("-1")
        else :
            top = queue[0]
            print(top)
    elif (a=="back"):
        if len(queue)==0:
            print("-1")
        else :
            top = queue[-1]
            print(top)
    elif (a=="size"):
        print(len(queue))
    elif (a=="empty"):
        if(len(queue)==0):
            print("1")
        else:
            print("0")
    elif (a=="pop"):
        if len(queue)==0:
            print("-1")
        else :
            top=queue.pop(0)
            print(top)
    else: #push
        b, c=a.split()
        c=int(c)
        queue.append(c)

    count=count+1