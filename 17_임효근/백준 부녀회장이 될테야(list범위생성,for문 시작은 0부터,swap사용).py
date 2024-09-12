T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    ZeroFloor = list(range(n))
    #print(ZeroFloor)
    ZeroFloor.append(n)
    #print(ZeroFloor)
    ZeroFloor.pop(0)
    #print(ZeroFloor)
    OverFloor = list(range(len(ZeroFloor)))
    #print(OverFloor)
    People = 0
    for g in range(k):
        People = 0
        for z in range(len(ZeroFloor)):
            People += ZeroFloor[z]
            #print(People)
            OverFloor[z] = People
        for z in range(len(ZeroFloor)):
            ZeroFloor[z],OverFloor[z] = OverFloor[z],ZeroFloor[z]
           
        print(ZeroFloor)
        print(OverFloor)
            
    print(ZeroFloor[n-1])
    #print(OverFloor)
