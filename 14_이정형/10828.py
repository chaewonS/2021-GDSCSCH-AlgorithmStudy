# -*- coding: utf-8 -*-
import sys

stack = []


def push(x):
    stack.append(x)


def pop():
    if not stack:
        return -1
    else:
        return stack.pop()


def size():
    return len(stack)


def top():
    if stack:
        return stack[-1]
    else:
        return -1


def empty():
    if stack:
        return 0
    else:
        return 1


# 총 몇개를 받을 건지
num = int(sys.stdin.readline())
# 함수 적용
for _ in range(num):
    input_split = sys.stdin.readline().split()
    order = input_split[0]

    if order == "push":
        push(input_split[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "top":
        print(top())
