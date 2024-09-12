N, M, R = map(int, input().split(' '))

A = []
for i in range(N):
    A.append(list(map(int, input().split(' '))))

#움직인 횟수
cnt = 0

#위,아래,왼,오
dx = [0,0,-1,1]
dy = [-1,1,0,0]

temp_of_idx = []
#현재 위치 
x,y = 0,0
while cnt != M*N:
    if x == y:
        temp_of_idx.append(x,y)
        
