string = input()

print(len(string.split()))

'''
# split을 서술해서 아래와 같이 구현해보려했는데 계속 틀렸다고 뜸..ㅠ

bl = 0
a = ' '
b = ' '
c = ' '
str = input()

for i in str :
    a = b
    b = c
    c = i
    if b == ' ' and a != ' ' and c != ' '  :
        bl += 1

print(bl+1)

'''
