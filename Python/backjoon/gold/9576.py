import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(M)]
    arr.sort(key=lambda x: (x[1], x[0]))
    book = [0 for i in range(1001)]
    idx = 0
    answer = 0
    for a, b in arr:
        for i in range(a, b + 1):
            if book[i] == 0:
                answer += 1
                book[i] = 1
                break
    print(answer)