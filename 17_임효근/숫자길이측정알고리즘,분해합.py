#주어진 값을 N으로 받고, 길이측정을 위해 K에 해당 값을 옮겨줌
N = int(input())
K = N
finish = False
#N의 길이를 측정하기 위한 변수
_lenN = 0


'''주어진 숫자의 자리수 크기를 파악하기 위한 코드
K를 10으로 나누면서 몫을 K에 저장하고, _lenN을 하나씩 증가시킨다.'''
while 0 < K:
    K //= 10
    _lenN += 1


for i in range(_lenN*9, 0, -1):          #for문을 거꾸로 돌리는 방법 2가지 
    if  N < i:                           #1)range를 reversed()로 감싸서 리스트를 뒤집기
        continue                         #2)range함수의 3번째 인자 step을 -1로 바꿔서 하나씩 감소하게 하기
    else :
        M = N - i                        #생성자 후보 M을 생성
        _strM = str(M)
        plusM = 0
        for z in range(len(str(M))):     #생성자 후보의 각 자리숫자 합 plusM을 생성
            plusM += int(_strM[z])
        if i == plusM:                   #plusM과 i가 일치하는 최초의 값이 최소값
            print(M)                     #M츨력
            finish = True                
            break

if finish == False:                      #위의 for문에서 결과가 안나왓을 때 o을 출력해주기 위한 것
    print(0)
