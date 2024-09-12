word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for croAlpha in croatia:
    if croAlpha in word:
        word = word.replace(croAlpha, '*')
print(len(word))

# 작동하지만 다른 코드가 더 쉽고 빠르게 동작
# word = input()
# count = idx = 0
# while idx < len(word):
#     if idx != len(word)-1:
#         if word[idx] in 'c':
#             if word[idx+1] in '=-':
#                 count+=1
#                 idx+=2
#                 continue
#         elif word[idx] in 'd':
#             if word[idx+1]=='-':
#                 count+=1
#                 idx+=2
#                 continue
#             elif word[idx+1:idx+3]=='z=':
#                 count+=1
#                 idx+=3            
#                 continue
#         elif word[idx] in 'ln' :
#             if word[idx+1]=='j':
#                 count+=1
#                 idx+=2
#                 continue
#         elif word[idx] in 'sz':
#             if word[idx+1]=='=':
#                 count+=1
#                 idx+=2
#                 continue
#     count+=1
#     idx+=1
# print(count)