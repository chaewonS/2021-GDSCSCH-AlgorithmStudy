import sys
a = list(map(int, sys.stdin.readline().split(' ')))
b = []
for i in range(a[1]):
    b.append(a[0])
print(b)


def func(li):
    if len(li) == 2:
        return li[0] * li[1]
    else:
        li_left = li[:int(len(li) / 2)]
        print(li_left)
        li_right = li[int(len(li) / 2):]
        print(li_right)
        return func(li_left) * func(li_right)


print(func(b))