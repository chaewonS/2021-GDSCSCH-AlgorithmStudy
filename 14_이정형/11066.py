# -*- coding: utf-8 -*-
import sys

# 테스트 데이터 개수
T = int(sys.stdin.readline())
# 소설을 구성하는 장의 수
# 1장 부터 K장까지 수록한 파일의 크기
for _ in range(T):
    pages = int(input())
    novel = [0] + list(map(int, sys.stdin.readline().split()))
    # 초기화
    stack_num = [0 for _ in range(pages + 1)]
    # stack_num은 누적합
    for i in range(1, pages + 1):
        stack_num[i] = stack_num[i - 1] + novel[i]

    # DP[i][j] : I부터 J까지 합하는데 필요한 최소 비용
    # DP활용해서 풀 것이며 이차원배열 형태로 만들어 풀이
    # 표로 따로 그려본 결과 다음과 같은 식으로 일반화할 수 있었음
    # DP[i][k] + DP[k+1][j] + sum(novel[i]~novel[j])
    # 2차원 배열 DP 생성
    DP = [[0 for i in range(pages + 1)] for _ in range(pages + 1)]
    # 나눈 부분의 파일 길이
    for i in range(2, pages + 1):
        # 시작점 정해주고 계산
        for j in range(1, pages + 2 - i):
            DP[j][j + i - 1] = min(
                [DP[j][j + k] + DP[j + k + 1][j + i - 1] for k in range(i - 1)]
            ) + (stack_num[j + i - 1] - stack_num[j - 1])

    print(DP[1][pages])
