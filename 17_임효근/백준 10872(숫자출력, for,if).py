N = int(input())
K=1
if N == 0 :
    print(1)
else :
    for i in range(1,N+1):
        #range의 끝부분은 -1해서 들어간다
        K *= i

    print(K)
