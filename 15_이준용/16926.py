from sys import stdin
input = stdin.readline

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n,m)//2):
        rowCur = i  #행 선택
        colCur = i  #열 선택
        save_bfr = arr[rowCur][colCur]

        for j in range(i+1, n-i):   #왼쪽(moveDown)
            rowCur = j
            save_aft = arr[rowCur][colCur]
            arr[rowCur][colCur] = save_bfr
            save_bfr = save_aft

        for j in range(i+1, m-i):   #아래쪽(moveRight)
            colCur = j
            save_aft = arr[rowCur][colCur]
            arr[rowCur][colCur] = save_bfr
            save_bfr = save_aft

        for j in range(i+1, n-i):   #오른쪽(moveUp)
            rowCur -= 1
            save_aft = arr[rowCur][colCur]
            arr[rowCur][colCur] = save_bfr
            save_bfr = save_aft
        
        for j in range(i+1, m-i):   #위쪽(moveLeft)
            colCur -= 1
            save_aft = arr[rowCur][colCur]
            arr[rowCur][colCur] = save_bfr
            save_bfr = save_aft

for i in arr:
    print(*i)