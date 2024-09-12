# 큰 동전부터 시작하는게 좋아보임 -> 돈은 오름차순으로 주어진다 했다.
# num은 돈의 종류 몇개 쓸건지, 총 얼마를 계산할 건지는 money
num, money = map(int, input().split())
# 어떤 종류의 돈을 지정할 건지 담아 둘 리스트
money_list = list()
# num 숫자만큼 돈의 종류 입력
for i in range(num):
    money_list.append(int(input()))

count = 0
# 내림차순으로 바꿔 큰 돈부터 계산하도록 하자
for i in reversed(range(num)):
    count += money // money_list[i]
    money = money % money_list[i]

# count 값 출력
print(count)
