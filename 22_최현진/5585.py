price = int(input())

money = 1000 - price

a = money // 500
temp = money % 500
b = temp // 100
temp %= 100
c = temp // 50
temp %= 50
d = temp // 10
temp %= 10
e = temp // 5
temp %= 5
f = temp
temp %= 1

result = a + b + c + d + e + f

if temp == 0:
    print(result)