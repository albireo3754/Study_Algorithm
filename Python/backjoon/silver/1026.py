import sys

input = sys.stdin.readline

N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort(reverse=True)
# print(arr1, arr2)
answer = 0
for i in range(N):
    answer += arr1[i] * arr2[i]
print(answer)