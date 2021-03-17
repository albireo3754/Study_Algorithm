import sys

input = sys.stdin.readline

# s >=

N, S = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))
answer = -1
def compare(a):
    global S
    global answer
    if a >= S:
        if answer == -1:
            answer = a
        answer = min(answer, a)

res = 0
start = 0
answer = 100000001
for i in range(N):
    res += arr[i]
    while res >= S and start <= i:
        answer = min(answer, i - start + 1)
        res -= arr[start]
        start += 1
if answer == 100000001:
    print(0)
else:
    print(answer)