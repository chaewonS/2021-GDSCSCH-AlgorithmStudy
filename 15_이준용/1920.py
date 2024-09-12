from sys import stdin

input = stdin.readline

def bianry_search(left, right, idx):
    mid = (left + right) // 2

    if left > right or mid > right:
        return 0

    if nums[idx] == a[mid]: #a 리스트에 nums[idx]가 있을경우
        return 1
    elif nums[idx] > a[mid]:    #f리스트의 오른쪽 탐색
        return bianry_search(mid+1, right, idx)
    else:   #리스트의 왼쪽 탐색
        return bianry_search(left, mid-1, idx)

n = int(input())
a = list(map(int, input().split())) #숫자 리스트

m = int(input())
nums = list(map(int, input().split()))  #찾아야 할 수
a.sort()

for idx in range(m):
    print(bianry_search(0, n-1, idx))