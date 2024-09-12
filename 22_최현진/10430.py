a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
result = 0

result = (a + b) % c
print(result)
result = ((a % c) + (b % c)) % c
print(result)
result = (a * b) % c
print(result)
result = ((a % c) * (b % c)) % c
print(result)
