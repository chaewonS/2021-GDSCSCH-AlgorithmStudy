#빠른 A + B

import sys
n = int(input())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split()) #정해진 개수의 정수를 한줄에 입력받을 때
    print(a + b)
