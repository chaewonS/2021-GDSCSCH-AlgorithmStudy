# -*- coding: utf-8 -*-
import sys

weight_cnt = int(input())
weight_list = list(map(int, sys.stdin.readline().split()))
bead_cnt = int(input())
beads_list = list(map(int, sys.stdin.readline().split()))
result = []
# 이 문제또한 DP로 풀 수 있는 문제
# 사실 왼쪽에 올린 거는 마이너스로 취급해야하는데 abs로 0기준 배열 오른쪽으로 복사 가능
# 파이썬엔 딕셔너리라는 좋은 자료형이 있음, False로 모두 초기화해주고 True로 바꿔줌으로써 가능한 숫자 알아내자
dp = [[False] * 15001 for _ in range(weight_cnt + 1)]
# 저울이 잴 수 있는 무게는 올려진 추들의 무게 차이
def calculate(num, chu):
    # 추 개수보다 많아지면 리턴
    if num > weight_cnt:
        return
    # 이미 True 값이 었다면 리턴
    if dp[num][chu]:
        return
    #  그거 또한 아니었다면 True
    dp[num][chu] = True

    # 아무것도안할 때, 왼쪽에 추올릴 때, 오른쪽에 추올릴떄에 대해 각각 재귀로 계산
    calculate(num + 1, chu + weight_list[num - 1])
    calculate(num + 1, abs(chu - weight_list[num - 1]))
    calculate(num + 1, chu)


# 초기화
calculate(0, 0)

for i in beads_list:
    if i > 15000:
        result.append("N")
        continue
    if dp[weight_cnt][i] == True:
        result.append("Y")
    else:
        result.append("N")

StrResult = " ".join(result)
print(StrResult)
