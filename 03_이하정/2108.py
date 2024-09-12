from collections import Counter

n=int(input())
k=[]
for i in range(n):
    k+=[int(input())]

k.sort()
# 산술평균
print(round(sum(k)/len(k)))
# 중앙값 (n은 항상 홀수)
if len(k)==1:
    print(k[0])
else:
    print(k[len(k)//2])
# 최빈값
d=Counter(k) # 리스트의 요소들의 개수를 세어, 딕셔너리 형태로 반환 {문자:개수}
m=[n for n in d.keys() if d[n] == max(d.values())] # 해당 요소가 최빈값인 경우 그 요소를 리스트로 저장
if len(m)==1:
    print(m[0])
else: # 최빈값이 2개 이상인 경우, 2번째로 작은 값 출력
    m.remove(min(m))
    print(min(m))
# 범위 
print(k[-1]-k[0])