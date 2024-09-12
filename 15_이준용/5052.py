from sys import stdin
input = stdin.readline
class Node:
    def __init__(self, data):
        self.link = [None for _ in range(10)]
        self.data = data
        self.isEnd = False

for _ in range(int(input())):
    root = Node('')
    cons = True
    for _ in range(int(input())):
        node = root
        ph_num = input().strip()
        for idx in range(len(ph_num)):
            num = int(ph_num[idx])

            temp = Node(num)
            if idx == len(ph_num)-1:
                temp.isEnd = True
            
            if node.link[num] == None:  #겹치는 번호가 없을경우
                node.link[num] = temp
                node = temp
            else:   #겹치는 번호일경우
                if temp.isEnd or node.link[num].isEnd:  #겹친 상태에서 추가된 번호 혹은 기존 번호가 끝난다면
                    cons = False
                    break
                node = node.link[num]
            
    print('YES') if cons else print('NO')