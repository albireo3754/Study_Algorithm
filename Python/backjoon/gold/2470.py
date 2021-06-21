import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

i = 0
j = N - 1
answer = [0, 0]
temp = 1000000000 * 2
while i < j:
    # print(i, j, temp, arr[i] + arr[j])
    if abs(arr[i] + arr[j]) < temp:
        answer = [arr[i], arr[j]]
        temp = abs(arr[i] + arr[j])
    if arr[i] + arr[j] < 0:
        i += 1
    else:
        j -= 1
print(*answer)