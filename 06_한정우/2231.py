a = int(input())
result = 0

for i in range(1, a+1):        
    x = list(map(int, str(i)))  
    y = i + sum(x)
    if(y == a):
        result = i                   
        break

print(result)