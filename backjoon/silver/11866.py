from collections import deque

q = deque()
q_pop = []

N, K = map(int,input().split(" "))
for i in range(N):
    q.append(i+1)

while len(q) > 0:
    for i in range(K):
        if i == K-1:
            q_pop.append(q.popleft())
            break
        q.append(q.popleft())

output = "<"

for i in range(len(q_pop)):
    if i == len(q_pop) - 1:
        output += f"{q_pop[i]}>"
        break
    output += f"{q_pop[i]}, "
print(output)

# 3 6 2 7 5 1 4
print(*q_pop)

# [3, 6, 2, 7, 5, 1, 4]
print(str(q_pop))

# <3, 6, 2, 7, 5, 1, 4>
print(f"<{str(q_pop)[1:-1]}>")