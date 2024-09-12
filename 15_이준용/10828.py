from sys import stdin

class Stack:
    stack = []
    head = -1

    def push(self, x):
        self.head+=1
        self.stack.insert(self.head, x)

    def pop(self):
        if self.empty(self):
            return self.head
        else:
            temp = self.stack[self.head]
            self.head-=1
            return temp

    def size(self):
        return self.head + 1

    def empty(self):
        if self.head == -1:
            self.stack.clear()
            return 1
        else:
            return 0

    def top(self):
        if self.empty(self):
            return self.head
        else:
            return self.stack[self.head]

functions = {
    'push' : Stack.push,
    'pop' : Stack.pop,
    'size' : Stack.size,
    'empty' : Stack.empty,
    'top' : Stack.top,
}
n = int(stdin.readline())
stack = Stack
for i in range(n):
    comm = stdin.readline().split()
    func = functions[comm[0]]
    if comm[0]=='push':
        func(stack, int(comm[1]))
    else:
        print(func(stack))