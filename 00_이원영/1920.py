import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
m = int(input())
s_ = list(map(int, input().split()))
s.sort()
for i in s_:
    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        if mid < n and mid > -1:
            if s[mid] < i: low = mid + 1
            else: high = mid - 1
        else: break
    if mid < n and mid > -1:
        if i == s[high + 1]: print(1)
        else: print(0)
    else: print(0)
