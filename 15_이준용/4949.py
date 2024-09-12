from sys import stdin
input = stdin.readline
while True:
    stack = []
    flag = False
    sentence = input() 
    if sentence == '.\n':
        break
    for letter in sentence:
        if letter in '([':
            stack.append(letter)
        elif letter==')':
            if len(stack) and stack.pop()=='(':
                continue
            else:
                flag = True
                break
        elif letter==']':
            if len(stack) and stack.pop()=='[':
                continue
            else:
                flag = True
                break
    if len(stack) or flag:
        print('no')
    else:
        print('yes')