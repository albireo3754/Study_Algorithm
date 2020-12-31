from sys import stdin

N = int(stdin.readline().rstrip())

members = []
for i in range(N):
    member = stdin.readline().rstrip().split(" ")
    member[0] = int(member[0])
    members.append(member)

members.sort(key= lambda x:x[0])
for member in members:
    print(f"{member[0]} {member[1]}")