import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split(' ')))
dp = [0 for i in range(n)]
answer = arr[0]
temp = arr[0]
dp[0] = arr[0]
if temp < 0:
    temp = 0

for i in range(1, n):
    dp[i] = max(dp[i - 1] + arr[i], arr[i])

# print(dp)
print(max(dp))
# for i in range(1, n):
#     temp += arr[i]
#     if temp < 0:
#         temp = 0
#     answer = max(answer, temp)
#     # print(answer)

# if temp == 0:
#     print(max(arr))
# else:
#     print(answer)
    

# print(arr)
