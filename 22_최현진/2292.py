n = int(input())

cnt = 1 # 방의 개수
tmp = 1

while n > tmp:
    tmp += 6 * cnt
    cnt += 1

print(cnt)