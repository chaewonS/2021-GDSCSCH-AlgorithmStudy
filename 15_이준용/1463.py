from sys import stdin

n = int(stdin.readline())

nums = [0 for _ in range(n+1)]
for i in range(2,n+1,1):
    #1을 빼는 연산은 2나 3으로 나누어지지 않는 연산에만 해당
    #미리 해주어도 2,3으로 나누어지는 연산에서는 min때문에 교체됨
    nums[i] = nums[i-1]+1 

    #2,3 모두 나누어지는 연산은 무엇이 최소인지 모르므로 둘 다 계산해야함
    if i%3==0:
        nums[i] =min(nums[i], 1 + nums[i//3])
    if i%2==0:
        nums[i] =min(nums[i], 1 + nums[i//2])
    
print(nums[n])