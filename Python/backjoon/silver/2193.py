n = int(input())
a, b, c = 1, 1, 2

if n == 1:
    print(1)
elif n == 2:
    print(1)
elif n == 3:
    print(2)
else:
    for i in range(n - 3):
        a, b, c = b, c, b + c
    print(c)