import sys

T = int(input())
for i in range(T):
    H, W, N = map(int ,sys.stdin.readline().rstrip().split(" "))
    floor = N % H
    room = N // H + 1
    if floor == 0:
        floor = H
        room = N // H
    if room < 10:
        print(f"{floor}0{room}")
    elif room >= 10:
        print(f"{floor}{room}")