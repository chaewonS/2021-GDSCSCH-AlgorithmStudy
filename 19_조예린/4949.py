while True:
    s = input()
    if s == '.':
        break

    stack = []
    result = True
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = False
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                result = False
                break
    
    if not stack and result == True:
        print('yes')
    else:
        print('no')