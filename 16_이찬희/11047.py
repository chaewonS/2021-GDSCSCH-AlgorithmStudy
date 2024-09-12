#N종류 동전으로 K원 만들기 

N, K = map(int,input().split())
Money = [int(input()) for _ in range(N)]

num = 0

for i in range(1, N+1): #N번 반복
    coin = Money[-1]

    if K>=coin: 
        n = K // coin  # n : 각 동전의 가치별 개수
        K -= coin*n 
        num += n
 
print(num)
