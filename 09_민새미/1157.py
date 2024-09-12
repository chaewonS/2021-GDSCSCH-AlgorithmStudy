i=input()

lists=[]
l=[]
count={}
cnt=0

for k in i:
    lists.append(ord(k))
    
# print(lists)

for x in lists:
    
    if x<97:
        x=x+32
    l.append(chr(x))
# print(l)



for p in l:
    try:count[p] +=1
    except : count[p]=1

# print(count)
ll=list(count.values())
# print(max(ll))
a=max(ll)

for key, value in count.items():
    if value==a: #큰 값이 같으면
        cnt=cnt+1
        k=key
        # print(cnt)
        

# print(cnt)
# print(k)
if cnt>=2:
    print("?")
else :
    print(k.upper())