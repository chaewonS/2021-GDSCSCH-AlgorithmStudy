def Hotel(H, W, N):
        
        if N > (H * W):
            return 1
        
        if N % H == 0:
            room = (N // H) +  (H * 100)
            
        else:
            room = (N // H + 1) + (N % H * 100)
        
        print(room)

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    Hotel(H, W, N)