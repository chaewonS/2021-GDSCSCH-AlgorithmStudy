n = int(input("input number : "))

#분해합
def Sum(n) :
    numstr = str(n) #문자열 변환
    s = n
    for i in range(len(numstr)) :
        s = s + int(numstr[i])
    return s

#생성자 찾기
def findCon(m) :
    for i in range(m) :
        if m == Sum(i) :
            return i
    return 0


print(findCon(n))