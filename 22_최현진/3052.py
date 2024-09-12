n = []
remainder = []
cnt = 0

for i in range(10):
    n.append(int(input()))
    num = n[i] % 42
    remainder.append(num) # 나머지를 리스트에 추가

remainder = set(remainder) # 리스트 -> 집합 : 중복 제거

print(len(remainder))