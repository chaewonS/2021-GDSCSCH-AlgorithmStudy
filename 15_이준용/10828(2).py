from sys import stdin
input = stdin.readline
class Stack:
    stack = []
    def push(self, num):
        self.stack.append(num)
    def pop(self):
        print(self.stack.pop()) if self.stack else print(-1)
    def size(self):
        print(len(self.stack))
    def empty(self):
        print(0) if self.stack else print(1)
    def top(self):
        print(self.stack[-1]) if self.stack else print(-1)
    func = {
        'push' : push,
        'pop' : pop,
        'size' : size,
        'empty' : empty,
        'top' : top
    }

stk = Stack
for _ in range(int(input())):
    comm= input().split()
    if len(comm)==2:
        stk.func[comm[0]](stk, int(comm[1]))
    else:
        stk.func[comm[0]](stk)