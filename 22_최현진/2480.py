a, b, c = map(int, input().split())
num = [a, b, c]

if num[0] == num[1] == num[2]: # 모두 같은 경우
    money = 10000 + num[0] * 1000

elif num[0] == num[1] or num[0] == num[2]: # 2개가 같은 경우
    money = 1000 + num[0] * 100

elif num[1] == num[2]: # 2개가 같은 경우
    money = 1000 + num[1] * 100
    
else: # 모두 다른 경우
    money = max(num) * 100

print(money)