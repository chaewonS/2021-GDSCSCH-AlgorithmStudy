from sys import stdin
input = stdin.readline
class Queue:
    queue = []
    def push(self, num):
        self.queue.append(num)
    def pop(self):
        print(self.queue.pop(0)) if self.queue else print(-1)
    def size(self):
        print(len(self.queue))
    def empty(self):
        print(0) if self.queue else print(1)
    def front(self):
        print(self.queue[0]) if self.queue else print(-1)
    def back(self):
        print(self.queue[-1]) if self.queue else print(-1)
    func = {
        'push' : push,
        'pop' : pop,
        'size' : size,
        'empty' : empty,
        'front' : front,
        'back' : back
    }

que = Queue
for _ in range(int(input())):
    comm = input().split()
    if len(comm)==2:
        que.func[comm[0]](que, comm[1]) 
    else:
        que.func[comm[0]](que)