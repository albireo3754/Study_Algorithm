from itertools import combinations
N, K = map(int,input().split(" "))

denominator = 1
numerator = 1

for i in range(N+1 - K, N+1):
    numerator *= i

for j in range(1, K+1):
    denominator *= j

print(numerator//denominator)