#분해합

n = int(input())

for i in range(1, n+1):  # map(function, iterable) : 함수, 반복가능한 자료형(리스트 , 튜플 등) / 반환값 : map 객체
    num = sum(map(int, str(i)))  #num에는 각 자리 수들의 합이 저장된다. 
    num_sum = i + num  # num_sum = 각 자리 수 합 + 숫자 = 분해합 

    if num_sum == n: 
        print(i)
        break
    if i == n: 
        print(0)
