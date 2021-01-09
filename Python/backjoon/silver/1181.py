import sys

N = int(input())

words = [""] * N
for i in range(N):
    words[i] = sys.stdin.readline().rstrip()

words = list(set(words))
for i in sorted(sorted(words), key = len):
    print(i)