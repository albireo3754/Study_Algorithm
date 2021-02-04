T = int(input())

test_case = []
for i in range(T):
    test_case.append(int(input()))

fib_upgrade = [(1, 0), (0, 1)]

for i in range(2, 41):
    fib_upgrade.append((fib_upgrade[i - 1][0] + fib_upgrade[i - 2][0], fib_upgrade[i - 1][1] + fib_upgrade[i - 2][1]))

for test in test_case:
    print(fib_upgrade[test][0], fib_upgrade[test][1])