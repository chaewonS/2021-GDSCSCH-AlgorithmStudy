# A~Z 65~90 a~z 97~122
import string

a = string.ascii_letters
b = string.ascii_uppercase
l = []
l_2 = []
s = input()
for i in range(len(a)):
    if a[i] in s:
        c = s.count(a[i])
        l.append(c)
    else:
        l.append(0)
for j in range(26):
    l_2.append(l[j] + l[j + 26])
if l_2.count(max(l_2)) > 1:
    print('?')
else:
    print(b[l_2.index(max(l_2))])
