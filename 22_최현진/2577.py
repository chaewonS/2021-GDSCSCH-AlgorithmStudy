A = int(input())
B = int(input())
C = int(input())

result = A * B * C
result = str(result)

count_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(10):
    print(result.count(count_list[i]))