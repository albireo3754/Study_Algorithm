import sys
import bisect

input = sys.stdin.readline

T = int(input())
A = int(input())
arrA = list(map(int, input().split()))

B = int(input())
arrB = list(map(int, input().split()))

# sumA = [0 for i in range(A)]
# sumA[0] = arrA[0]
# for i in range(1, A):
#     sumA[i] = sumA[i - 1] + arrA[i]
    
# sumB = [0 for i in range(B)]
# sumB[0] = arrB[0]
# for i in range(1, B):
#     sumB[i] = sumB[i - 1] + arrB[i]

sumA = []
sumB = []
for i in range(A):
    temp = 0
    for j in range(i, A):
        temp += arrA[j]
        sumA.append(temp)
for i in range(B):
    temp = 0
    for j in range(i, B):
        temp += arrB[j]
        sumB.append(temp)

# print(sumA, sumB)
# for i in range(1, A):
#     for j in range(0, i):
#         sumA.append(sumA[i] - sumA[j])
# for i in range(1, B):
#     for j in range(0, i):
#         sumB.append(sumB[i] - sumB[j])

# print(sumA)
# print(sumB)
sumB.sort()
answer = 0
for a in sumA:
    i = bisect.bisect(sumB, T - a)
    j = bisect.bisect_left(sumB, T - a)
    answer += i - j
    # print(a, sumB[i])
    # if i > 0 and T - a == sumB[i - 1]:
    #     answer += 1
# bisect.bisect()
# print(bisect.bisect([2], 0))
print(answer)
