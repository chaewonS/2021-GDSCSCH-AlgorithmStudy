from sys import stdin

lans = []
k, n = map(int, stdin.readline().split())
for i in range(k):
    lans.append(int(stdin.readline()))

left = 1
right = sum(lans)
length = right // 2

maxCnt = right//n

while True:
    if left>=length or left>=right:
        break
    
    if maxCnt >= length:
        counter = 0
        for lan in lans:
            counter += lan//length
    
        if counter >= n:
            left = length
            length = (right+left)//2

        elif counter < n:
            right = length
            length = (right+left)//2
    else:
        right = length
        length = (right+left)//2

print(left)