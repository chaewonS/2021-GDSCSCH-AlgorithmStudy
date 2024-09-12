from sys import stdin
input = stdin.readline
class DQueue:
    Dqueue = []
    Dqueue.insert
    def push_front(self, num):
        self.Dqueue.insert(0, num)
    def push_back(self, num):
        self.Dqueue.append(num)
    def pop_front(self):
        print(self.Dqueue.pop(0)) if self.Dqueue else print(-1)
    def pop_back(self):
        print(self.Dqueue.pop()) if self.Dqueue else print(-1)
    def size(self):
        print(len(self.Dqueue))
    def empty(self):
        print(0) if self.Dqueue else print(1)
    def front(self):
        print(self.Dqueue[0]) if self.Dqueue else print(-1)
    def back(self):
        print(self.Dqueue[-1]) if self.Dqueue else print(-1)
    func = {
        'push_front' : push_front,
        'push_back' : push_back,
        'pop_front' : pop_front,
        'pop_back' : pop_back,
        'size' : size,
        'empty' : empty,
        'front' : front,
        'back' : back
    }

que = DQueue
for _ in range(int(input())):
    comm = input().split()
    if len(comm)==2:
        que.func[comm[0]](que, comm[1]) 
    else:
        que.func[comm[0]](que)