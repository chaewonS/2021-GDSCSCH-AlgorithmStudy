#알람 시계 

H = int(input())
M = int(input())

print(H,":",M)

if H == 0 :
    if M >= 45 :
        H = 0
        M = M -45
        print(H, M)
    else :
        H = 23
        M = M + 15
        print(H, M)
elif H > 0 :
    if M >= 45 :
        M = M -45
        print(H, M)
    else :
        H = H - 1
        M = M + 15
        print(H, ":", M)
