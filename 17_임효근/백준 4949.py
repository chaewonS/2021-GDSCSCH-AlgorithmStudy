while 1:
    #문장을 검사하기 위해 필요한 변수들을 선언해준다
    stack = ["trap"]
    isItCorrect = True
    i = 0

    
    #문장을 읽어온다. 이 때, 문장의 처음에 .이 오면 프로그램을 종료한다.
    sentence = input()
    if(sentence[0] == "."):
        break

    while 1:
        #.가 오면 문장의 마지막이므로 루프를 종료한다
        if(sentence[i] =="."):
            break
        #(나 [가 오면 stack변수에 저장한다(실제로는 list이다)
        if(sentence[i] == "(" or sentence[i] =="["):
            stack.append(sentence[i])
        #)나 ]가 오면 stack에 마지막으로 저장된 변수를 pop한다. 이렇게하면 stack에선 pop된 변수가 지워지므로 list를 stack처럼 사용할 수 있다.
        if(sentence[i] == ")" or sentence[i] == "]"):
            lastIn = stack.pop()
            #만약 )나]가 먼저온 경우에는 루프자체를 끝낸다 
            if(lastIn == "trap"):
                isItCorrect = False
                break
            #괄호의 짝이 안 맞는 두가지 경우의 수를 거르고 나면 괄호의 짝이 맞는 경우만 남는다.
            if(lastIn =="(" and sentence[i] == "]"):
                isItCorrect = False
                break
            elif(lastIn =="[" and sentence[i] == ")"):
                isItCorrect = False
                break
        i+=1
    
    #닫는 괄호가 없는 경우엔 stack의 길이가 1보다 크게 된다. 이럴 경우도 틀린 경우이다.
    if(len(stack) != 1):
        isItCorrect = False
    
    #isItCorrect변수가 False인 경우엔 no, True인 경우엔 yes를 출력해준다.
    if(isItCorrect == True):
        print("yes")
    else:
        print("no")
