import sys

input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    arr.sort()
    a, b, c = arr
    if c == 0:
        break
    if c ** 2 - b ** 2 == a ** 2:
        print('right')
    else:
        print('wrong')