a,b,c = input().split()
a = int(a)
b= int(b)
c = int(c)

list = []
list.append(a);
list.append(b);
list.append(c);

list = sorted(list)

print(str(list[0]) + " " + str(list[1]) + " " + str(list[2]))
