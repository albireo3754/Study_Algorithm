import sys

input = sys.stdin.readline

(N, d, k, c) = map(int, input().split())
rail = []
for _ in range(N):
    rail.append(int(input()))

ds = [0 for _ in range(d + 1)]
eats = set(rail[-k:])
eats.add(c)

temp = 0
for i in range(N - k, N):
    ds[rail[i]] += 1
    if ds[rail[i]] == 1:
        temp += 1
ds[c]+=1
if ds[c] == 1:
    temp += 1
result = temp
for i in range(N):
    # print(temp, i, i - k)
    # print(ds)

    ds[rail[i - k]] -= 1
    ds[rail[i]] += 1
    
    # eats.remove(rail[i - k])
    # eats.add(rail[i])
    if rail[i] == rail[i - k]:
        continue
    if ds[rail[i - k]] == 0:
        temp -= 1
    if ds[rail[i]] == 1:
        temp += 1
    # eats.add(c)
    result = max(result, temp)

print(result)

