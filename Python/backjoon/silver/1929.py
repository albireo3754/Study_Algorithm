import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())
isPrime = [True for i in range(M + 1)]
primes = []
def sieve(M):
    for i in range(2, math.ceil(M ** 0.5) + 1):
        if isPrime[i]:
            # primes.append(i)
            j = i + i
            while j <= M:
                isPrime[j] = False
                j += i

sieve(M)
<<<<<<< HEAD
isPrime[0] = False
isPrime[1] = False
=======
>>>>>>> 24d78c483f6d5670e87720aa83f46fb86f46d499
for i in range(N, M + 1):
    if isPrime[i]:
        print(i)