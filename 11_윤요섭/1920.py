import sys
from typing import Counter
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split(' ')))
counter_a = Counter(a)
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split(' ')))
for i in range(m):
    if counter_a[b[i]] > 0:
        print(1)
    else:
        print(0)