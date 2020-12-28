from sys import stdin

N = input()
for _ in range(int(N)):
    inputs = stdin.readline().rstrip().split(" ")
    print(int(inputs[0]) + int(inputs[1]))