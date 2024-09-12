input = int(input())
for i in range(1,input+1):
    sum_int = sum(map(int,str(i)),i)
    if input == sum_int:
        print(i)
        break
    if input == i:
        print(0)
