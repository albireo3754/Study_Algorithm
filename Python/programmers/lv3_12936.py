def solution(n, k):
    num = [i for i in range(0, n + 1)]
    answer = []
    n_fac = 1
    for i in range(1, n + 1):
        n_fac *= i
    print(n_fac)
    while n > 0:
        n_fac = n_fac // n
        for i in range(1, len(num)):
            if k <= n_fac * i:
                answer.append(num.pop(i))
                n -= 1
                k -= n_fac * (i - 1)
                break
        #result를 
    return answer