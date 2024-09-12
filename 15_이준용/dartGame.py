def solution(dartResult):
    i = 0
    answer = ['', '', '']
    for temp in dartResult:
        if temp in 'SDT*#':
            if temp == 'S':
                answer[i] = int(answer[i])
            elif temp == 'D':
                answer[i] = pow(int(answer[i]), 2)
            elif temp == 'T':
                answer[i] = pow(int(answer[i]), 3)
            elif temp == '*':
                for j in range(i-1, i-3, -1):
                    if j>=0: answer[j] *= 2
                continue
            else: #temp == '#'
                answer[i-1] *= -1
                continue
            i+=1
        else:
            answer[i] += temp
    return sum(answer)