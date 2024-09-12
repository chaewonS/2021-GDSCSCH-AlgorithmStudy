#팩토리얼

num1 = int(input())
num2 = 1

if num1 == 0 :
    print(1)
else : 
    for i in range(num1) :   #range(n) : 0~ n-1의 범위
        num2 = (i+1)*num2
    print(num2)


