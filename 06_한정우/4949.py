import sys 
input = sys.stdin.readline

sen = input().rstrip()
while sen != '.': 
    stack = [] 
    result = 1 
    for i in sen: 
        if i == '(' or i == '[': 
            stack.append(i) 
        elif i == ')': 
            if stack and stack[-1] == '(': 
                stack.pop() 
            else: 
                result = 0 
                break 
        elif i == ']': 
            if stack and stack[-1] == '[': 
                stack.pop() 
            else: 
                result = 0 
                break 
    print("yes" if result and not(stack) else "no")
    
    sen = input().rstrip() 
