from sys import stdin

def pow(a, b, c): #a^b
    #나머지 연산은 분배법칙 가능 => 각 return값마다 나머지 연산 실행
    if b == 1:
        return a % c

    x = pow(a, b//2, c)
    
    if b%2 == 0:
        return x*x%c
    else:
        return x*x*a%c
# def pow(a,b,c):
#     temp = 1
#     while(b):
#         if b & 1:   #n이 짝수이면 false 홀수이면 true (0001 AND (xxx0 or xxx1))
#             temp  = temp * a % c
#         a  = a*a%c
#         b = b//2


a, b, c = map(int, stdin.readline().split())

print(pow(a,b,c))