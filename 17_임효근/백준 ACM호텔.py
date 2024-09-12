T = int(input())


for i in range (T):
    H,W,N = map(int,input().split( ))
    Y=1
    X=1
    CaseBreak = True
    #H:층,W:방번호,N:몇번째 손님
    FullH = H
    while(1):
        if FullH > N :
            Y = N - (FullH - H)
            print("%d%02d"%(Y,X))
            CaseBreak = False
            break
        elif FullH == N:
            Y = H
            print("%d%02d"%(Y,X))
            CaseBreak = False
            break
        
        X += 1
        FullH += H
