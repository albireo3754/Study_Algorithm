import sys

input = sys.stdin.readline

min_, max_ = map(int, input().split(' '))

i = 2
squares = []
while i**2 <= max_:
    squares.append(i**2)
    i += 1
result = [1 for i in range(min_, max_ + 1)]
for square in squares:
    j = min_ // square
    while j * square < min_:
        j += 1

    while j * square <= max_:
        result[j * square - min_] = 0
        j += 1

print(sum(result))


