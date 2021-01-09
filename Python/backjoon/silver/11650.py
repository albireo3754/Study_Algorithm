import sys

point = []
for i in range(int(input())):
    point.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

point.sort(key=lambda x: (x[0], x[1]))

for i in point:
    print(f"{i[0]} {i[1]}")