import sys
import bisect
input = sys.stdin.readline

N = int(input())
edge = {}
lines = []
b = set()
for i in range(N):
    lines.append(list(map(int, input().split(' '))))
    edge[lines[i][1]] = lines[i][0]
    b.add(lines[i][1])
lines.sort(key = lambda x: x[0])
# print(lines)

dp = [lines[0][1]]
back = [-1 for i in range(500001)]
size = 1

for i in range(1, N):
    if dp[-1] < lines[i][1]:
        back[lines[i][1]] = dp[-1]
        dp.append(lines[i][1])
    else:
        temp = lines[i][1]
        change_pos = bisect.bisect_left(dp, temp)
        # print(temp, dp)
        if change_pos - 1 >= 0:
            back[temp] = dp[change_pos - 1]
        else:
            back[temp] = -1
        dp[change_pos] = temp

lis = dp[-1]
while lis >= 0:
    # print(lis)
    b.remove(lis)
    lis = back[lis]
a = []
for i in b:
    a.append(edge[i])
print(len(a))
for i in sorted(a):
    print(i)