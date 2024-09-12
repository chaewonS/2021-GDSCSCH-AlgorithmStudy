word = input().upper()
usage = {}

for alpha in word:
    if alpha in usage:
        usage[alpha] += 1
    else:
        usage[alpha] = 1

maxWord = ''
for key, val in usage.items():
    if val == max(usage.values()):
        maxWord+=key
if len(maxWord)==1:
    print(maxWord)
else:
    print('?')