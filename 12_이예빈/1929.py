# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 2부터 n의 제곱까지 나머지 존재 여부 확인
def isPrime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    
M, N = map(int, input().split())

for n in range(M,N+1):
    if(isPrime(n)):
        print(n)