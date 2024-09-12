def ch_Conquer(n1,n2):
    area1 = n1
    area2 = n2
    area3 = min(n1,n2) * 2
    return max(area1,area2,area3)

def Conquer(n1,n2,wide):
    height = min(n1,n2)
    area = wide * height

        
def str_to_int (k):
    n = int(k)
    return n

while(True):
    n = (input().split(' '))
    if n[0] == '0':
        break
    else:
        n.remove(n[0])

        print(n)
        
