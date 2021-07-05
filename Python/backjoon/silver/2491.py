import sys
import bisect
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# lis_asc = [arr[0]]
# lis_des = [arr[0]]

# def bisect_right(arr, val):
#     left, right = 0, len(arr) - 1
#     answer = 0
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] < val:
#             right = mid - 1
#             answer = mid
#         else:
#             left = mid + 1
#     return answer

# # print(bisect_right([4,3,2,2,1], 2))
# # print(bisect.bisect_right([1,2,3,3,4], 3))
# for i in range(1, N):
#     if lis_asc[-1] <= arr[i]:
#         lis_asc.append(arr[i])
#     else:
#         j = bisect.bisect_right(lis_asc, arr[i])
#         lis_asc[j] = arr[i]
#     if lis_des[-1] >= arr[i]:
#         lis_des.append(arr[i])
#     else:
#         j = bisect_right(lis_des, arr[i])
#         lis_des[j] = arr[j]
# print(lis_asc, lis_des)
# print(len(lis_asc) if len(lis_asc) > len(lis_des) else len(lis_des))

asc = [arr[0]]
des = [arr[0]]
answer = 0
for i in range(1, N):
    if len(asc) == 0 or asc[-1] <= arr[i]:
        asc.append(arr[i])
    else:
        answer = max(answer, len(asc))
        asc = [arr[i]]
    if len(des) == 0 or des[-1] >= arr[i]:
        des.append(arr[i])
    else:
        answer = max(answer, len(des))
        des = [arr[i]]
    print(asc, des)
answer = max(len(asc), len(des), answer)
print(asc, des)
print(answer)