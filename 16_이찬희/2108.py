#통계학- 산술평균 중앙값 최빈값 범위

from collections import Counter  #최빈값 구하기 위함

num1 = int(input())  
num = []
for i in range(num1) :
    num2 = int(input())
    num.append(num2)

k=Counter(num).most_common() #데이터의 개수가 많은 순으로 정렬된 배열(튜플)을 반환하는 함수

if num1 == 1 : 
    exp = num1 
    med = num1
    mod = num1
    ran = 0
    print(exp, med, mod, ran)

else : 
    exp = round(sum(num) / num1) #반올림 round() - 기본값 : 소수 첫째 자리
    med = num[num1//2] 
    if k[0][1] == k[1][1] : # k = (숫자, 개수) 이런식으로 반환 즉, 최빈값이 여러개 있으면 두번째 값을 출력한다. 
        mod = k[1][0]
    else :
        mod = k[0][0]
    
    print("exp :",exp)  
    print("med :",med)
    print("mod :",mod)
    ran = max(num) - min(num)
    print("ran :",ran)




