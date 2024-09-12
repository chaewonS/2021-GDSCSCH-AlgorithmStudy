def solution(n, arr1, arr2):
    arr3 = []
    answer = []
    for i in range(n):
        arr3.append(arr1[i] | arr2[i])
    
    for i in range(n):
        bin_temp = bin(arr3[i])
        binary = str(bin_temp)
        answer_temp = ''
        a = len(binary) - n
        for j in binary[a:]:
            if j == '1':
                j = '#'
            else : 
                j = ' '
            answer_temp += j
        answer.append(answer_temp)
    return answer
