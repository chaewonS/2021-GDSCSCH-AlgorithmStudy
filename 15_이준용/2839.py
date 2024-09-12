from sys import stdin

n = int(stdin.readline())
box = [2000 for _ in range(n+2+1)]  #인덱스 오류 피하기 위해 2를 더해주어 무조건 box[5]까지 나오게

box[3],box[5] = 1,1

for i in range(6,n+1,1):
    box[i] = min(box[i-3], box[i-5]) + 1

if box[n] >= 2000:
    print(-1)
else:
    print(box[n])