sugar = int(input())

a = sugar // 5
temp = sugar % 5

if temp % 3 == 0:
    b = temp // 3
    result = a + b
    print(a + b)

else:
    if a >= 1:
        for i in range(1,  a + 1):
            temp2 = temp + 5 * i

            if temp2 % 3 == 0:
                b = temp2 // 3
                a -= i
                print(a + b)
                break
            elif i == a:
                print(-1)
                

    else:
        print(-1)