line = input()
stack = []
count = i = 0
while i<len(line):
    if line[i] == '(':
        if line[i+1] == ')':
            count += len(stack)
            i+=1            
        else:
            stack.append('(')
            count+=1
    else:stack.pop()
    i+=1
print(count)