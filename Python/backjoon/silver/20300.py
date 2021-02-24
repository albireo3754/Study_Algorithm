import sys

input = sys.stdin.readline

N = int(input())

losss = list(map(int, input().split(' ')))

losss.sort()
i = 0
j = N - 1
max_loss = 0
if N % 2 == 1:
    j = N - 2
    max_loss = losss[-1]

while i < j:
    max_loss = max(max_loss, losss[i] + losss[j])
    i += 1
    j -= 1
print(max_loss)