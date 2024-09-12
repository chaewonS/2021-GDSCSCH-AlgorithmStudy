engToNum = {
    'zero' : '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}
numL = [str(i) for i in range(10)]
def solution(s):
    answer = engStr = ''
    for letter in s:
        if letter in numL:            
            answer+=letter
        else:
            engStr+=letter
            try:
                answer += engToNum[engStr]
                engStr = ''
            except:
                pass
    return int(answer)

numString = input()
print(solution(numString))