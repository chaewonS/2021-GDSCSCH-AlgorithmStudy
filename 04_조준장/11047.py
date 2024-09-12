import sys

n, k = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(n)]
coin.sort(reverse=True) # 큰 동전부터 사용하기 위해 내림차순으로 정렬
cnt = 0 # 개수

# 반복문을 통해 동전을 사용
for i in range(n):

    # 동전의 가치가 필요로 하는 가치보다 작거나 같을 경우
    if k >= coin[i]:

        # 필요로 하는 가치를 동전으로 나눈다.
        # 몫은 동전의 개수로 카운트하고 나머지는 다시 k의 값으로 초기화시킨다.
        a, k = divmod(k, coin[i])
        cnt += a

    # 필요로 하는 가치가 0이 되면 반복을 멈춘다.
    if k == 0:
        break

# 동전의 개수 출력
print(cnt)
