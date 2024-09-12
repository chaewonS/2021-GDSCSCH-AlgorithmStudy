# 방법 1

phone = input()
time = 0

num = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

for i in range(len(num)):
    for j in range(len(num[i])):
        if i == 0:
            phone = phone.replace(num[i][j], '2')
        elif i == 1:
            phone = phone.replace(num[i][j], '3')
        elif i == 2:
            phone = phone.replace(num[i][j], '4')
        elif i == 3:
            phone = phone.replace(num[i][j], '5')
        elif i == 4:
            phone = phone.replace(num[i][j], '6')
        elif i == 5:
            phone = phone.replace(num[i][j], '7')
        elif i == 6:
            phone = phone.replace(num[i][j], '8')
        elif i == 7:
            phone = phone.replace(num[i][j], '9')
        
for k in phone:
    time += (int(k))

time += len(phone)

print(time)

# 방법 2(효율적?)

# phone = input()
# time = 0

# num = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

# for unit in num:
#     for i in unit:
#         for j in phone:
#             if i == j:
#                 time += num.index(unit) + 3

# print(time)