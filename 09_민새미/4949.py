# 하나 또는 여러줄에 걸쳐서 문자열이 주어진다.
# 각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 길이는 100글자보다 작거나 같다.
# 입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.

#yes가 계속 안나오게 하는 법...어떻게 하는거지

stack =[]
while(1):
    i = input()

    if(i[-1]!='.'):
        print("입력의 종료조건으로 맨 마지막에 점이 들어와야합니다!")
        print("no")
        
    else:

        for x in i:
            #print(x)
            if x =='{' or x== '[' or x=='(' :
                # print(x)
                stack.append(x)

            elif x=="]":
                if(len(stack)<1):
                    print("no")
                else:
                    top=stack.pop()
                    if(top!="["):
                        print("no")
                        # print("괄호가 맞지 않습니다")
                        
                        break
                    else:
                        print("yes")
                        # print("괄호 잘 맞췄습니다")
                        
            elif x==")":
                if(len(stack)<1):
                    print("no")
                else:
                    top=stack.pop()
                    if(top!="("):
                        print("no")
                        # print("괄호가 맞지 않습니다")
                        break
                    else:
                        print("yes")
                        # print("괄호 잘 맞췄습니다")
        stack=[]    


# while True :
#     a = input()
#     stack = []

#     if a == "." :
#         break

#     for i in a :
#         if i == '[' or i == '(' :
#             stack.append(i)
#         elif i == ']' :
#             if len(stack) != 0 and stack[-1] == '[' :
#                 stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
#             else : 
#                 stack.append(']')
#                 break
#         elif i == ')' :
#             if len(stack) != 0 and stack[-1] == '(' :
#                 stack.pop()
#             else :
#                 stack.append(')')
#                 break
#     if len(stack) == 0 :
#         print('yes')
#     else :
#         print('no')
        