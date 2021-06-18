import sys

input = sys.stdin.readline

N = int(input())
string = input().rstrip()

answer = string[0]
def calc(a, op, b):
    if op == '+':
        return int(a) + int(b)
    elif op == '*':
        return int(a) * int(b)
    else:
        return int(a) - int(b)
def div_conq(value, i):
    if i + 1 == N:
        return value
    a = calc(value, string[i + 1], string[i + 2])
    if i + 4 < len(string):
        temp = calc(string[i + 2], string[i + 3], string[i + 4])
        b = calc(value, string[i + 1], temp)
        # if i == 0:
            # print(a, b)
            # print(div_conq(a, i + 2), div_conq(b, i + 4))
        return max(div_conq(a, i + 2), div_conq(b, i + 4))
    else:
        return div_conq(a, i + 2)
    
print(div_conq(answer, 0))