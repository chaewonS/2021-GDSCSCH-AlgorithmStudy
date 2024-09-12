
i = int(input())
count=0
stack=[]

while(i>count):

    print(stack)
    a= input()


    if (a=="top"):
        if len(stack)==0:
            print("-1")
        else :
            top = stack[-1]
            print(top)
    elif (a=="size"):
        print(len(stack))
    elif (a=="empty"):
        if(len(stack)==0):
            print("1")
        else:
            print("0")
    elif (a=="pop"):
        if len(stack)==0:
            print("-1")
        else :
            top=stack.pop()
            print(top)
    else: #push
        b, c=a.split()
        c=int(c)
        stack.append(c)

    count=count+1