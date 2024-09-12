import sys

result=1
a=int(sys.stdin.readline())
while a :
    result=a*result
    a=a-1
    
    if a==0:
        print(result)
        break