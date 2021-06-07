import sys

input = sys.stdin.readline

LEFT = 'L'
RIGHT = 'D'
INSERT = 'P'
DELETE = 'B'

string = input().rstrip()
T = int(input())
cursor = len(string)
s1 = [i for i in string]
s2 = []

for i in range(T):
    # print(string)
    raw_cmd = input().rstrip()

    if raw_cmd == LEFT:
        if len(s1) != 0:
            s2.append(s1.pop())
    elif raw_cmd == RIGHT:
        if len(s2) != 0:
            s1.append(s2.pop())
    elif raw_cmd == DELETE:
        if len(s1) != 0:
            s1.pop()
    else:
        # INSERT
        cmd, char = raw_cmd.split()
        s1.append(char)
print(''.join(s1) + ''.join(reversed(s2)))