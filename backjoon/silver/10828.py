from sys import stdin

class Stack:
    DO = 3
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        if self.size()>0:
            return self.stack.pop()
        return -1
    def size(self):
        return len(self.stack)

    def empty(self):
        if self.size():
            return 0
        return 1
    def top(self):
        if self.empty():
            return -1
        return self.stack[-1]

N = int(stdin.readline().rstrip())
stack = Stack()
for _ in range(N):
    command = stdin.readline().rstrip().split(" ")
    if command[0] == 'push':
        stack.push(command[1])
    elif command[0] == 'top':
        print(stack.top())
    elif command[0] == 'size':
        print(stack.size())
    elif command[0] == 'empty':
        print(stack.empty())
    elif command[0] == 'pop':
        print(stack.pop())