s, nums = input().split()

info = {  # 각자 LCD 번호중 몇번이 on 해야 하는지 리스트를 통해서 표현한다. 진짜 LCD판처럼 생각하는 것
    '0': [1, 2, 3, 4, 5, 6],
    '1': [3, 6],
    '2': [2, 3, 4, 5, 7],
    '3': [2, 3, 5, 6, 7],
    '4': [1, 3, 6, 7],
    '5': [1, 2, 5, 6, 7],
    '6': [1, 2, 4, 5, 6, 7],
    '7': [2, 3, 6],
    '8': [1, 2, 3, 4, 5, 6, 7],
    '9': [1, 2, 3, 5, 6, 7]
}
s = int(s)  #문자열로 입력한 s 변수를 정수형으로 바꿔준다.
answer = [
    [[' ' for i in range(s + 2)] for j in range(2 * s + 3)]  #???
    for k in range(len(nums))
]


def lines(board, idx):
    for i in idx:
        if i == 1:
            for j in range(1, s + 1):
                board[j][0] = '|'
        elif i == 2:
            for j in range(s):
                board[0][j + 1] = '-'
        elif i == 3:
            for j in range(1, s + 1):
                board[j][s + 1] = '|'
        elif i == 4:
            for j in range(s + 1, 2 * s + 1):
                board[j + 1][0] = '|'
        elif i == 5:
            for j in range(s):
                board[2 * s + 2][j + 1] = '-'
        elif i == 6:
            for j in range(s + 2, 2 * s + 2):
                board[j][s + 1] = '|'
        elif i == 7:
            for j in range(s):
                board[s + 1][j + 1] = '-'


for i, num in enumerate(nums):
    lines(answer[i], info[num])

for i in range(2 * s + 3):
    for j in range(len(nums)):
        if j == len(nums) - 1:
            print(''.join(answer[j][i]))
        else:
            print(''.join(answer[j][i]), end=' ')
