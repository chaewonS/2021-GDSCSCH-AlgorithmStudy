a, b, c = input().split()
a = int(a)
b = int(b)
c= int(c)
max = a
if a==b and a==c:
    print(a*1000 + 10000)
elif a==b or a==c:
    print(a*100+1000)
elif b==c:
    print(b*100+1000)
else:
    if a>b and a>c:
        print(a*100)
    elif b>a and b>c:
        print(b*100)
    else:
        print(c*100)

