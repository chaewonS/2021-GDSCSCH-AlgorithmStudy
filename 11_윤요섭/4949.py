while True:
    o = 0
    c = 0
    g_l = []  #가로 리스트
    n = input()  #문자열 입력
    if n[0] == '.':  #종료 조건
        break
    for i in range(len(n)):
        if n[i] == '(' or n[i] == '[':
            o += 1
            g_l.append(n[i])
        elif n[i] == ')' or n[i] == ']':
            c += 1
            if c > o:
                g_l.append(1)
                break
            if g_l[-1] == '(' and n[i] == ')' or g_l[-1] == '[' and n[i] == ']':
                g_l.pop()

    if len(g_l) == 0:

        print('yes')
    else:
        print('no')