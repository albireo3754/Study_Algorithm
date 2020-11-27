# 0 - time out! Refer other solution
# 100 %


def gcd(A, B):
    while A >= 0:
        if A % B == 0:
            return B
        elif A>=B:
            A, B = A % B, B
        else:
            A, B = B % A, A
            
def isPrimeDiv(gcdab, A, B):
    gcdWithdiv = gcdab
    
    while gcdWithdiv >= 1:
        A = A//gcdWithdiv
        if A == 1:
            break
        gcdWithdiv = gcd(gcdWithdiv, A)
        if gcdWithdiv == 1:
            return False

    gcdWithdiv = gcdab
    
    while gcdWithdiv >= 1:
        B = B//gcdWithdiv
        if B == 1:
            break
        gcdWithdiv = gcd(gcdWithdiv, B)
        if gcdWithdiv == 1:
            return False
    
    return True
def solution(A, B):
    # write your code in Python 3.6
    cnt = 0
    gcds = []
    Z = len(A)
    for i in range(Z):
        gcds.append(gcd(A[i], B[i]))
    
    for i in range(Z):
        if isPrimeDiv(gcds[i], A[i], B[i]):
            cnt += 1
    
    return cnt
