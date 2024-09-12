from sys import stdin

sum = []
while True:
    try:
        a, b = map(int, stdin.readline().split())
        sum.append(a+b)
    except:
        break

for num in sum:
    print(num)