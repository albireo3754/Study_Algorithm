import sys

input = sys.stdin.readline
meets = []
N = int(input())
for i in range(N):
    meets.append(list(map(int, input().split(' '))))

meets.sort(key = lambda x: (x[1], x[0]))

idx = 0
end_time = meets[idx][1]
answer = 1
while idx < N - 1:
    idx += 1
    if meets[idx][0] >= end_time:
        answer += 1
        end_time = meets[idx][1]

print(answer)