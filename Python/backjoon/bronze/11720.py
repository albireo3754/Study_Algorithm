from sys import stdin
N = int(input())

second_line = stdin.readline().rstrip()
output = 0
for i in range(N):
    output += int(second_line[i])
print(output)