# -*- coding: utf-8 -*-
import sys

arr = []
for i in range(10):
    n = int(sys.stdin.readline().strip())
    arr.append(n % 42)

# 중복제거를 위해 set 사용
arr = list(set(arr))
print(len(arr))
