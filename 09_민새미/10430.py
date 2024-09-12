A=int(input())
B=int(input())
C=int(input())

if(((A and B) and C)>=2 and ((A and B) and C)<=10000):
    print((A+B)%C)
    print(((A%C) + (B%C))%C)
    print((A*B)%C)
    print(((A%C) * (B%C))%C)
else:
    print("A, B, C 값은 2이상 10000이하로 입력하셔야 합니다.")