import sys
import math
input = sys.stdin.readline

N = int(input())

MINT = "mint chocolate"
TOOTH = "toothpaste"
exp = input().rstrip().split(' ')
answer = [0 for i in range(100001)]

def do(oper, val):
    if val < 0:
        val *= -1

    sqrtval = math.ceil((math.sqrt(val) + 1))
    if oper == '*':
        for i in range(2, sqrtval):
            while val % i == 0:
                answer[i] += 1
                val = val // i

        if val > 1:
            answer[val] += 1

    elif oper == '/':
        for i in range(2, sqrtval):
            while val % i == 0:
                answer[i] -= 1
                val = val // i

        if val > 1:
            answer[val] -= 1

oper = '*'
zero = False
for i in range(N):
    val = int(exp[2 * i])
    if val == 0:
        zero = True
        break
    if i == 0:
        do('*', val)
    else:
        do(exp[2 * i - 1], val)

if zero:
    print(MINT)
else:
    for i in range(2, 100001):
        if answer[i] < 0:
            print(TOOTH)
            break
    else:
        print(MINT)
# print(answer)

