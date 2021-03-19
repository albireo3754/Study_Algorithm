
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    clothes = {}
    for i in range(int(input())):
        a, b = input().rstrip().split(' ')
        if b not in clothes:
            clothes[b] = 2
        else:
            clothes[b] += 1
    answer = 1
    for i in list(clothes.values()):
        answer *= i
    print(answer - 1)
