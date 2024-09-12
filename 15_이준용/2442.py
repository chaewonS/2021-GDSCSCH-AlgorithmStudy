n = int(input())
length = n
for line in range(n):
    for char in range(length):
        if(char <  n-line-1):
            print(' ',end='')
        else:
            print('*',end='')
    length += 1
    print('')
