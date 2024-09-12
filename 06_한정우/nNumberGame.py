def solution(n, t, m, p):
    answer = ''
    
    count=""
    num = 0
    while len(count)<((t-1)*m+p):
        a = convert(n,num)
        a = a[::-1]
        count += a
        num+=1
    
    for i in range((t-1)*m+p):
        if i%m == p-1:
            answer += count[i]
    return answer

def convert(n,num): 
    ex = "0123456789ABCDEF"
    arr = ""
    arr += ex[num%n]
    if num//n >= n:
        arr += convert(n,num//n)
    else:
        if num//n != 0:
            arr +=ex[num//n]
    
    return arr