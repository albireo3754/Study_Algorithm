import sys

listen_N, see_M = map(int, sys.stdin.readline().split(' '))

listen = set()
see = set()
for i in range(listen_N):
    listen.add(sys.stdin.readline().rstrip())
for j in range(see_M):
    see.add(sys.stdin.readline().rstrip())

listen_see = listen.intersection(see)
print(len(listen_see))
for i in sorted([*listen_see]):
    print(i)