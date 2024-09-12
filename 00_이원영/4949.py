while True :
    stack = []
    flag = 0

    str = input()

    if str == '.' :
        break

    for i in str :
        if i == '(' :
            stack.append(i)
        elif i == ')' :
            if len(stack) == 0 or stack[-1] != '(' :
                flag = 1
                break
            else :
                stack.pop()
        elif i == '[' :
            stack.append(i)
        elif i == ']' :
            if len(stack) == 0 or stack[-1] != '[' :
                flag = 1
                break
            else :
                stack.pop()

    if flag == 0 and len(stack) == 0 :
        print("yes")
    else :
        print("no")
