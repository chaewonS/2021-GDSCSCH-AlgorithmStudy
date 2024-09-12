from sys import stdin


result = []
def backtracking():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for num in range(1, n+1):
        if num not in result:
            result.append(num)
            backtracking()
            result.pop()
    
n, m = map(int, stdin.readline().split())
backtracking()