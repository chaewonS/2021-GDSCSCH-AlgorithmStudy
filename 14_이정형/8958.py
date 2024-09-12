import sys

N = int(sys.stdin.readline())

for _ in range(N):
    ox_list = list(sys.stdin.readline())
    score = 0
    sum_score = 0
    for ox in ox_list:
        if ox == "O":
            score += 1
            sum_score += score
        elif ox == "X":
            score = 0
    print(sum_score)
