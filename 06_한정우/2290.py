import sys

count = sys.stdin.readline().split()
size = int(count[0])
nums = []

width = size + 2
height = 2*size + 3

for i in range(len(count[1])):
    nums.append(count[1][i])

# 가로*높이*숫자 개수 리스트 초기화 
array = [[[0 for _ in range(width)] for _ in range(height)] for _ in range(len(count[1]))]


for i in range(len(nums)):
    if nums[i] == '1':
        for j in range(height-1):
            if j == 0 or j==int(height/2):
                continue
            array[i][j][width-1] = 1    
    elif nums[i] == '2':
        for j in range(height):
            if j == 0 or j == height-1 or j == int(height/2):
                for n in range(1,width-1):
                    array[i][j][n] = 2
            elif j<int(height/2):
                array[i][j][width-1] = 1
            elif j>int(height/2):
                array[i][j][0] = 1
    elif nums[i] == '3':
        for j in range(height):
            if j == 0 or j == height-1 or j == int(height/2):
                for n in range(1, width-1):
                    array[i][j][n] = 2
            else:
                array[i][j][width-1] = 1
    elif nums[i] == '4':
        for j in range(1,height-1):
            if j == int(height/2):
                for n in range(1, width-1):
                    array[i][j][n] = 2
            elif j<int(height/2):
                array[i][j][0] = 1
                array[i][j][width-1] = 1
            elif j>int(height/2):
                array[i][j][width-1] = 1
    elif nums[i] == '5':
        for j in range(height):
            if j == 0 or j == height - 1 or j == int(height/2):
                for n in range(1, width-1):
                    array[i][j][n] = 2
            elif j<int(height/2):
                array[i][j][0] = 1
            elif j>int(height/2):
                array[i][j][width-1] = 1
    elif nums[i] == '6':
        for j in range(height):
            if j == 0 or j == height - 1 or j == int(height/2):
                for n in range(1, width-1):
                    array[i][j][n] = 2
            elif j<int(height/2):
                array[i][j][0] = 1
            elif j>int(height/2):
                array[i][j][0] = 1
                array[i][j][width-1] = 1
    elif nums[i] == '7':
        for j in range(height-1):
            if j == 0:
                for n in range(1, width-1):
                    array[i][j][n] = 2
            elif j != int(height/2):
                array[i][j][width-1] = 1
    elif nums[i] == '8':
        for j in range(height):
            if j == 0 or j == height - 1 or j == int(height/2):
                for n in range(1, width-1):
                    array[i][j][n] = 2
            elif j<int(height/2):
                array[i][j][0] = 1
                array[i][j][width-1] = 1
            elif j>int(height/2):
                array[i][j][0] = 1
                array[i][j][width-1] = 1
    elif nums[i] == '9':
        for j in range(height):
            if j == 0 or j == height - 1 or j == int(height/2):
                for n in range(1, width-1):
                    array[i][j][n] = 2
            elif j<int(height/2):
                array[i][j][0] = 1
                array[i][j][width-1] = 1
            elif j>int(height/2):
                array[i][j][width-1] = 1
    elif nums[i] == '0':
        for j in range(height):
            if j == 0 or j == height - 1:
                for n in range(1, width-1):
                    array[i][j][n] = 2
            elif j<int(height/2):
                array[i][j][0] = 1
                array[i][j][width-1] = 1
            elif j>int(height/2):
                array[i][j][0] = 1
                array[i][j][width-1] = 1


for i in range(height):
    for c in range(len(nums)):
        for j in range(width):
            if array[c][i][j] == 0:
                print(' ',end='')
            elif array[c][i][j] == 1:
                print('|',end='')
            elif array[c][i][j] == 2:
                print('-',end='')
        print(' ',end='')
    print('')