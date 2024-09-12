s ,n = input().split()

length = len(n)
s = int(s)
row = s+2
col = s*2+3

def printSpace():   #모두 빈 공간   ex) ...
    for i in range(row): print(' ', end='')

def printMiddle():  #중앙만 '-'     ex) .-.
    print(' ', end='')
    for i in range(s): print('-', end='')
    print(' ', end='')

def printSide():    #좌우측만 '|'   ex) |.|
    print('|', end='')
    for i in range(s): print(' ', end='')
    print('|', end='')
def printRight():   #우측만 '|'     ex) ..|
    for i in range(row-1): print(' ', end='')
    print('|', end='')
def printLeft():    #좌측만 '|'     ex) |..
    print('|', end='')
    for i in range(row-1): print(' ', end='')

def Zero(cur):
    if cur == 1 or cur == col:  #커서가 첫번째 줄과 마지막 줄일때
        printMiddle()
    elif cur == row:    #커서가 중앙일때
        printSpace()
    else:
        printSide()
def One(cur):
    if cur==1 or cur==row or cur==col:
        printSpace()
    else:
        printRight()
def Two(cur):
    if 1<cur<row:
        printRight()
    elif row<cur<col:
        printLeft()
    else:
        printMiddle()
def Three(cur):
    if cur==1 or cur==row or cur==col:
        printMiddle()
    else:
        printRight()
def Four(cur):
    if cur==1 or cur==col:
        printSpace()
    elif 1<cur<row:
        printSide()
    elif cur==row:
        printMiddle()
    else:
        printRight()
def Five(cur):
    if 1<cur<row:
        printLeft()
    elif row<cur<col:
        printRight()
    else:
        printMiddle()
def Six(cur):
    if cur==1 or cur==row or cur==col:
        printMiddle()
    elif 1<cur<row:
        printLeft()
    else:
        printSide()
def Seven(cur):
    if cur==1:
        printMiddle()
    elif cur==row or cur==col:
        printSpace()
    else:
        printRight()
def Eight(cur):
    if cur==1 or cur==row or cur==col:
        printMiddle()
    else:
        printSide()
def Nine(cur):
    if cur==1 or cur==row or cur==col:
        printMiddle()
    elif 1<cur<row:
        printSide()
    else:
        printRight()

funcDict = {
    0:Zero,
    1:One,
    2:Two,
    3:Three,
    4:Four,
    5:Five,
    6:Six,
    7:Seven,
    8:Eight,
    9:Nine
}

for i in range(1, col+1, 1):
    for j in range(length):
        num = int(n[j])
        funcDict[num](i)
        if j<length-1:
            print(' ', end='')
    print('')