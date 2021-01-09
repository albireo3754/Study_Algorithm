from collections import deque
import sys

q = deque()
for i in range(int(input())):
    command = sys.stdin.readline().rstrip().split(" ")
    if command[0] == "push":
        q.append(command[1])
    elif command[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        print(q[0] if len(q) != 0 else -1)
    elif command[0] == "back":
        print(q[-1] if len(q) != 0 else -1)
        