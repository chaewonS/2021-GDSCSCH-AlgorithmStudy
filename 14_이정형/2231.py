import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    num = sum((map(int, str(i))))  # 각 자릿수를 더하기 위해 str 변환후 map 함수 사용
    decom_num = i + num  # 분해합 = 생성자 수 + 각 자릿수의 합
    if decom_num == n:  # 이 분해합 값이 입력값과 같다면 출력 후 break
        print(i)
        break

else:
    print(0)
