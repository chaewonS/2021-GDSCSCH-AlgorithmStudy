def solution(n, arr1, arr2):
    answer = ['' for _ in range(n)]

    for i in range(n):
        for _ in range(n): 
            temp1 = arr1[i]%2
            arr1[i]//=2
            temp2 = arr2[i]%2            
            arr2[i]//=2

            if temp1 or temp2:
                answer[i] = '#' + answer[i]
            else:
                answer[i] = ' ' + answer[i]
    return answer