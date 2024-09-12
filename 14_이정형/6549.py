# -*- coding: utf-8 -*-
import sys
from collections import deque

# 스택 구조로 풀기 위해 공부..
# 만약 스택에 있는 높이보다 더 높은 높이가 나오면 push
# 만약 스택에 있는 높이보다 더 낮은 높이가 나오면 pop한 후 최소높이에 대한 정보 저장
# 높이는 이걸로 해결하고 너비는 어떻게 할까
# 너비는 왼쪽서 부터 이동한다고 할 때 pop을 한 후 저장된 부분부터 그 다음 pop을 하는 구간 전 구간까지가 너비다.
# 하지만 중간에 높이가 1, 4, 5, 1처럼 나온다면 첫번째 1에서 스택이 비어있지 않은 상태가 발생
# 다시 1로 돌아왔을때의 i값과 스택에 남아있는 i값 그리고 1을 빼주면 된다.
while True:
    nemo = list(map(int, sys.stdin.readline().split()))
    # 첫번째 시작점 설정 pop(0)
    n = nemo.pop(0)

    # 아무것도 없을 때
    if n == 0:
        break
    # 스택과 큐의 기능을 지원하는 함수 deque 사용(초기화)
    # deque를 하면 리스트형태로 저장
    stack = deque()
    result = 0
    # 왼쪽부터 차례로
    for i in range(n):
        # 0입력시 컷
        while len(stack) != 0 and nemo[stack[-1]] > nemo[i]:
            tmp = stack.pop()  # 스택을 건들면 안되니까 temp 사용

            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1
            result = max(result, width * nemo[tmp])
        stack.append(i)  # 스택쌓기

    # 스택을 비워주기 (마지막까지 또 더 넓은게 있을 수 있으니까)
    while len(stack) != 0:
        tmp = stack.pop()

        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] - 1
        result = max(result, width * nemo[tmp])

    print(result)
