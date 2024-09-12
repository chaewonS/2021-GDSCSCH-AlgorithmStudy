# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def rotate(a):
    # temp 초기화
    top = matrix[a][a]
    left = matrix[n - a - 1][a]
    bottom = matrix[n - a - 1][m - a - 1]
    right = matrix[a][m - a - 1]

    # top
    for i in range(a + 1, m - a):
        matrix[a][i - 1] = matrix[a][i]
    # left
    for i in range(n - a - 1, a, -1):
        matrix[i][a] = matrix[i - 1][a]
    # bottom
    for i in range(m - a - 1, a + 1, -1):
        matrix[n - a - 1][i] = matrix[n - a - 1][i - 1]
    # right
    for i in range(a + 1, n - a):
        matrix[i - 1][m - a - 1] = matrix[i][m - a - 1]
    # finish
    matrix[a + 1][a] = top
    matrix[n - a - 1][a + 1] = left
    matrix[n - a - 2][m - a - 1] = bottom
    matrix[a][m - a - 2] = right


n, m, r = map(int, input().split())
# n X m인 배열, 반시계 방향으로 돌리기
matrix = [list(map(int, input().split())) for _ in range(n)]
# temp 공간에 옮긴 후 이전 공간에서 돌리는 식으로 하면 될 것 같다.

inside = n if n <= m else m
for _ in range(r):
    for i in range(inside // 2):
        rotate(i)

for row in matrix:
    print(*row)
