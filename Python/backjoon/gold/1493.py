import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

# length, width, height이지만, 의미가 중요 X 크기만 중요함
x, y, z = map(int, input().split())
N = int(input())
arr = {}
for i in range(N):
    a, b = map(int, input().split())
    if b > 0:
        arr[2 ** a] = b

# print(arr)
def div_conq(x, y, z):
    # print(x, y, z, arr)
    if len(arr) == 0:
        return -1
    if x == y and y == z and x == z and x in arr:
        arr[x] -= 1
        if arr[x] == 0:
            del arr[x]
        return 1
    answer = []

    if z > y:
        for i in range(2):
            answer.append(div_conq(x, y, z // 2))
    elif y > x:
        for i in range(2):
            answer.append(div_conq(x, z // 2, y // 2))
            answer.append(div_conq(x, y // 2, z // 2))
    else:
        for i in range(8):
            answer.append(div_conq(x // 2, y // 2, z // 2))
    # print(x,y,z,answer)
    if -1 in answer:
        return -1
    
    return sum(answer)

x, y, z = sorted([x, y, z])
print(div_conq(x, y, z))