# 1. 50
# 2. this is gcd problem - 100

def gcd(a, b, res):
    if a == b:
        return res*a
    elif (a % 2 == 0) and (b % 2 == 0):
        return gcd(a // 2 , b // 2 , res * 2)
    elif (a % 2 == 0):
        return gcd(a // 2, b, res)
    elif (b % 2 == 0):
        return gcd(a , b // 2, res)
    elif a > b:
        return gcd(a - b, b, res)
    else:
        return gcd(a, b - a, res)

def solution(N, M):
    # write your code in Python 3.6
    X = 0
    wrapper = []
    cnt = 0

    gcdiv = gcd(N, M, 1)
    lcm = N * M // gcdiv

    return lcm // M
