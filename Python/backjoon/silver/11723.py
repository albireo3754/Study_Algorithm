import sys

input = sys.stdin.readline
S = set()

M = int(input())
for i in range(M):
    command = input().rstrip()
    oper = ''
    num = 0
    if command == "all" or command == "empty":
        oper = command
    else:
        oper, _num = command.split(' ')
        num = int(_num)
    if oper == "add":
        S.add(num)
    elif oper == "check":
        if num in S:
            print(1)
        else:
            print(0)
    elif oper == "remove":
        if num in S:
            S.remove(num)
    elif oper == "toggle":
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif oper == "all":
        S = set([i for i in range(1, 21)])
    elif oper == "empty":
        S.clear()

