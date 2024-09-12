import sys

input = sys.stdin.readline
# 입력값
n = int(input())
# 재귀함수로 팩토리얼 기능 구현
def factorial(n):
    result = 1
    if n > 0:
        result = n * factorial(n - 1)
    return result


print(factorial(n))
