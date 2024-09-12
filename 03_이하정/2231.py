n=int(input())

for i in range (1,n+1):
    d=i
    for k in str(i): # i의 각 자리수를 str으로 반환
        d+=int(k)
    if d==n:
        res=i
        break
    else:
        res=0
print(res)