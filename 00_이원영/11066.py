import sys
input = sys.stdin.readline

def dp(start,end):
		# 메모이제이션이 된 구간
        if d[start][end] != -1:
            return d[start][end]
        
        if start == end:
            return 0
        
        ans = float('inf')
        s = sum(f[start:end+1])
        for i in range(start, end):
        	# 양분할 한 것 각각 + 둘을 합친 것
            temp = dp(start,i) + dp(i+1,end) + s
            
            if ans > temp:
                ans = temp
            
            d[start][end] = ans
        return ans

for i in range(int(input())):
    n = int(input())
    f = list(map(int,input().split()))
    d = [[-1]*(n+1) for i in range(n+1)]
    
    print(dp(0,n-1))
