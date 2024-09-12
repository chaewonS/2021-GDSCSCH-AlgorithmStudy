n, k = map(int,input().split())
money=[]
for j in range(n):
    money+=[int(input())]
cnt=0
for i in range(1,len(money)+1):
    q,k=divmod(k,money[-i])
    cnt+=q
print(cnt)