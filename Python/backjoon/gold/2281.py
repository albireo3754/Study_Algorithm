import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))
dp = [-1 for i in range(1001)]

def find_min(start):
    if dp[start] != -1:
        return dp[start]
    if start == N - 1:
        dp[start] = 0
        return dp[start]
    ret = 10000000000
    res = M
    for i in range(start, N):
        #한칸 띄우기
        if i != start:
            res -= 1
        if res - arr[i] < 0:
            break
        #마지막줄 조건 == index가 N-1까지 진행됨 -> dp[start] = 0
        if i == N - 1:
            res = 0
            dp[start] = 0
            return dp[start]
        else:
            res -= arr[i]
            ret = min(ret, res ** 2 + find_min(i + 1))
    dp[start] = ret
    return dp[start]
print(find_min(0))
# print(dp)