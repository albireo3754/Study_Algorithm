# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, P, Q):
    # write your code in Python 3.6
    
    # N is max integer
    # M is p.len()
    M = len(P)

    primes = [0 for _ in range(N + 1)]
    primes[1] = 1
    prime = []

    i = 2
    while i <= int(N**0.5):
        if primes[i] == 0:
            primes[i] = 0
            prime.append(i)
            j = 2
            while i * j <= N:
                primes[i * j] = i
                j += 1
        i += 1


    # for i in range(2,len(primes)):
    #     if primes[i] == 0:
    #         prime.append(i)
        
    semiPri = [0 for _ in range(N + 1)]

    for i in prime:
        j = 4
        while j<=N:
            if j % i == 0:
                if primes[j//i] == 0:
                    semiPri[j] = 1
            j += 1


    query = [0 for _ in range(N+1)]
    for i in range(1,len(semiPri)):
        query[i] = query[i-1] + semiPri[i]


    
    return [query[Q[i]] - query[P[i]-1] for i in range(len(P))]


    
    
