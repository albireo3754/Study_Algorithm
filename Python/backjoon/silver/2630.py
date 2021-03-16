import sys

input = sys.stdin.readline

N = int(input().rstrip())

paper = []
answer = [0, 0, 0]

for i in range(N):
    paper.append(list(map(int, input().split(' '))))

def divide(x, y, size):
    if size == 1:
        return paper[x][y]
    
    a = divide(x, y, size // 2)
    b = divide(x + size // 2, y, size // 2)
    c = divide(x, y + size // 2, size // 2)
    d = divide(x + size // 2, y + size // 2, size // 2)

    if a == b == c == d:
        if size == N:
            answer[a] += 1
        return a
    else:
        answer[a] += 1
        answer[b] += 1
        answer[c] += 1
        answer[d] += 1
        return 2

divide(0, 0, N)
for i in range(2):
    print(answer[i])