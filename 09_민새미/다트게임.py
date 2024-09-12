i=input()

res=0
count=0

for x in i:
    k=ord(x)
    print(k)
    count=count+1
    p=0 #첫 판 점수
    q=0 #두번재 판 점수
    z=0 #세번째 판 점수
    chk=0 #옵션 중첩 확인
    

    if(count==1): #첫 판
        if(48<= k<=57): #점수 숫자
            a=chr(k)
            
        elif (k==83): #S:1제곱
            b=a^1
        elif (k==68): #D:2제곱
            b=a^2
        elif (k==84): #T:3제곱
            b=a^3
    
        if (k==42): # *: 이전 값에 2곱, 현재 값에 2곱
            chk=1
            c=b*2
            p=c
            count=count+1
            
        elif (k==35): # #: 이전 값에 2곱, 현재 값에 2곱
            chk=2
            c=b-2
            p=c
            count=count+1
            
        elif (chk==1 and k==35) or (chk==2 and k==42):
            c=c/2
            c=b*-2
            p=c
            count=count-1

    elif(count==2):
        if(48<= k<=57): #점수 숫자
            a=chr(k)
            
        elif (k==83): #S:1제곱
            b=a**1
        elif (k==68): #D:2제곱
            b=a**2
        elif (k==84): #T:3제곱
            b=a**3
    
        if (k==42): # *: 이전 값에 2곱, 현재 값에 2곱
            chk=1
            c=b*2
            q=p*2
            q=c
            count=count+1
            
        elif (k==35): # #: 마이너스
            chk=2
            c=b-2
            q=c

            count=count+1
            
        elif (chk==1 and k==35) or (chk==2 and k==42):
            c=c/2
            c=b*-2
            q=c
            count=count-1

    elif(count==3):
        if(48<= k<=57): #점수 숫자
            a=chr(k)
            
        elif (k==83): #S:1제곱
            b=a^1
        elif (k==68): #D:2제곱
            b=a^2
        elif (k==84): #T:3제곱
            b=a^3
    
        if (k==42): # *: 이전 값에 2곱, 현재 값에 2곱
            chk=1
            c=b*2
            z=q*2
            z=c
            count=count+1
            
        elif (k==35): # #: 마이너스
            chk=2
            c=b-2
            z=c

            count=count+1
            
        elif (chk==1 and k==35) or (chk==2 and k==42):
            c=c/2
            c=b*-2
            z=c
            count=count-1

    res=p+q+z

print(res)