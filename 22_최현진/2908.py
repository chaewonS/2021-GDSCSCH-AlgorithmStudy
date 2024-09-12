num = input().split()

num[0] = "".join(reversed(num[0])) # slice 이용한 방법: num[0][::-1]
num[1] = "".join(reversed(num[1]))

print(max(num))