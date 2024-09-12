from collections import Counter
from sys import stdin
def arithmetic_geometric_mean(n, NumList=[]):
    return round(sum(NumList)/n)
def median(n, NumList=[]):
    if n==1:
        return NumList[0]    
    NumList.sort()
    return (NumList)[int((n)/2)]

def mode(n, NumList=[]):
    if n==1:
        return NumList[0]    
    count = Counter(NumList).most_common()

    modes = []
    for num in count:
        if num[1] == count[0][1]:
            modes.append(num[0])

    modes.sort()
    if len(modes) > 1:
        return modes[1]
    else:
        return modes[0]

def rng(n, NumList=[]):
    if n == 1:
        return 0
    NumList.sort()
    return NumList[-1]-NumList[0]

n = int(stdin.readline())
NumList = []
for i in range(n):
    NumList.append(int(stdin.readline()))

print(arithmetic_geometric_mean(n, NumList))
print(median(n, NumList))
print(mode(n, NumList))
print(rng(n, NumList))