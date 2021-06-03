import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
T = int(input())

male = 1
female = 2
for _ in range(T):
    sex, number = map(int, input().split())
    if sex == male:
        temp = number
        while number <= N:
            arr[number - 1] = arr[number - 1]^1
            number += temp
    elif sex == female:
        arr[number - 1] = arr[number - 1] ^ 1
        temp = 1
        while 0 <= number - 1 - temp and temp + number - 1 < N:
            left = (number - 1) - temp
            right = temp + number - 1
            if arr[left] == arr[right]:
                arr[left] = arr[left]^1
                arr[right] = arr[right]^1
                temp += 1
            else:
                break


j = 0
for i in range(N):
    j += 1
    if j == 20:
        print(arr[i])
        j = 0
    else:
        print(arr[i], end=' ')
        