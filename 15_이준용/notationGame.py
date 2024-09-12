def solution(n, t, m, p):
    answer = ''
    count = num = 0
    while True:
        notted_num = notation(n, num)
        for idx in range(len(notted_num)):
            if count%m+1 == p:
                answer += notted_num[idx]
            if len(answer)==t:
                return answer
            count+=1
        num+=1

def notation(n, num):
    result = ''
    alpha = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    if not num:
        return '0'
    while num>0:
        num, mod = divmod(num, n)
        if mod < 10:
            result = str(mod)+result
        else:
            result = alpha[mod]+result            
    return result