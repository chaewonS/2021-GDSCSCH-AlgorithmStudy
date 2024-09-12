def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        a = bin(arr1[i]|arr2[i])[2:]
        while len(a) != n:
            a = "0" + a
        c = ""
        for j in range(len(a)):
            if a[j] == "1":
                c = c + "#"
            elif a[j] == "0":
                c = c + " "
            
        answer.append(c)
    return answer