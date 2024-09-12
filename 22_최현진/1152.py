sentence = input()
cnt = 0

for i in range(len(sentence)):
        if sentence[i] == ' ':
            cnt += 1

if sentence[0] == ' ':
    cnt -= 1
if sentence[len(sentence) - 1] == ' ':
    cnt -= 1

result = cnt + 1
print(result)