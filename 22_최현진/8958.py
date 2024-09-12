n = int(input())
answer = []

for i in range(n):
    total = 0
    current = 1
    answer.append(input())

    for j in answer[i]:
        if j == 'O':
            total += current
            current += 1

        elif j == 'X':
            if current > 1:
                current = 1

    print(total)