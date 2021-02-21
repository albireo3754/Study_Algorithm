import sys

input = sys.stdin.readline

N, K = map(int, input().split(' '))

seq = list(map(int, input().split(' ')))
i = 0
j = 0
count = [0 for i in range(100001)]
answer = 0
while j < len(seq):
    if count[seq[j]] >= K:
        answer = max(answer, j - i)
        print(i, j)
        while count[seq[j]] < K - 1:
            count[seq[i]] -= 1
            i += 1
    count[seq[j]] += 1
    j += 1
print(answer)