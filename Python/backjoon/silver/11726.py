import sys

input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    fib = [0, 1, 2]
    for i in range(3, n + 1):
        fib.append((fib[i - 1] + fib[i - 2]) % 10007)
    print(fib[n])