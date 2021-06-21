import sys
# sys.setrecursionlimit(100000)
input = sys.stdin.readline

# length, width, height이지만, 의미가 중요 X 크기만 중요함
x, y, z = map(int, input().split())
N = int(input())
arr = []
for i in range(N):
    a, b = map(int, input().split())
    if b > 0:
        arr.append(((2 ** a) ** 3, 2 ** a, b))
arr.sort()
volume = x * y * z
# print(arr, volume)
answer = 0
while arr or volume > 0:
    cube_volume, n, cnt = arr.pop()
    if volume >= cube_volume:
        while volume > 0 and cnt > 0:
            volume -= cube_volume
            answer += 1
            cnt -= 1
print(answer)


# # print(arr)
# possible = True
# def div_conq(x, y, z):
#     # print(x, y, z, arr)
#     global possible
#     if not possible or len(arr) == 0:
#         possible = False
#         return -1
#     if x == 0 or y == 0 or z == 0:
#         return 0
#     answer = []
#     # answer.append(div_conq())

#     n = min(x, y, z)
#     # print(x, y, z)
#     while n > 0:
#         # print(x-n, y-n, z-n, x,y,z,n)
#         if n in arr:
#             answer.append(1)
#             arr[n] -= 1
#             if arr[n] == 0:
#                 del arr[n]
#             answer.append(div_conq(x, y, z - n))
#             answer.append(div_conq(x, y - n, n))
#             answer.append(div_conq(x - n, n, n))
#             break
#         n = n // 2
#     # print(x,y,z,answer, n)
#     if not possible or -1 in answer or len(answer) == 0:
#         possible = False
#         return -1
    
#     return sum(answer)

# x, y, z = sorted([x, y, z], reverse=True)
# print(div_conq(x, y, z))