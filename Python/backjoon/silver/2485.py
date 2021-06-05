import sys

input = sys.stdin.readline

N = int(input())

arr = [int(input()) for i in range(N)]

arr.sort()

subs = []
for i in range(1, N):
    subs.append(arr[i] - arr[i - 1])

def gcc(a, b):
    # must a > b
    if b > a:
        a, b = b, a

    while b > 0:
        a, b = b, a % b
    return a

g = subs[0]
# print(subs)
for i in range(1, len(subs)):
    g = gcc(g, subs[i])

# sol 1
# answer = 0
# for i in range(0, N - 1):
#     tree = arr[i]
#     while tree + g < arr[i + 1]:
#         answer += 1
#         tree += g

# sol 2
answer = sum(map(lambda sub: sub // g - 1, subs))
print(answer)

# print(g)
# print(gcc(2, 4), '=== gcc must 2')
# print(gcc(12, 7))
# print(gcc(5, 7))
# print(gcc(6, 21))

