n = int(input())

a, b, c = 1, 1, 2

if n == 0:
    print(0)
elif n == 1:
    print(a)
elif n == 2:
    print(b)
elif n == 3:
    print(c)
else:
    for i in range(3, n):
        a, b, c = b, c, b + c
    print(c)
    