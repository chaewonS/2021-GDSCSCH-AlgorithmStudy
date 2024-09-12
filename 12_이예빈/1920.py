# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

n = int(input())
n_list = list(map(int, input().split(' ')))
n_list.sort()
target_n = int(input())
targets = list(map(int, input().split(' ')))

# 이진탐색
def binary(target):
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if n_list[mid] == target:
            return True

        if target < n_list[mid]:
            right = mid-1
        elif target > n_list[mid]:
            left = mid + 1
        
        
for i in range(target_n):
    if(binary(targets[i])==True):
        print(1)
    else:
        print(0)
    