import sys

pocketmons = dict()

N, M = map(int, sys.stdin.readline().split(' '))

for i in range(1, N + 1):
    pocketmon = sys.stdin.readline().rstrip()
    pocketmons[pocketmon] = i
    pocketmons[str(i)] = pocketmon

print('-------------------------------')
for i in range(M):
    print(pocketmons[sys.stdin.readline().rstrip()])
