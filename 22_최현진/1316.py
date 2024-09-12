n = int(input())

for i in range(n):
    word = input()
    for j in range(len(word) - 1):
        if word[j] == word[j + 1]: # 연속해서 나타나면
            pass
        elif word[j] in word[j + 1:]: # 떨어져서 나타나면
            n -= 1
            break

print(n)