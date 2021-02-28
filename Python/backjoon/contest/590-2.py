import sys

input = sys.stdin.readline

N, K = map(int, input().split(' '))
def make_some(N, K):
    answer = []
    while K >= N:
        answer.append(N)
        N -= 1
        K -= N
    answer.append(K + 1)
    answer.extend([i for i in range(1, N + 1) if i != K + 1])
    return answer
print(*make_some(N, K))

