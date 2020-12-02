# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def fib(A,B):
    if len(A) <= 1:
        return [1,1]

    L = max(A) + 1
    maxVal = 2 ** (max(B)) 

    fibs = [1,1]
    for i in range(2,L):
        fibs.append((fibs[i-1] + fibs[i-2]) % maxVal) 
    return fibs
def solution(A, B):
    # write your code in Python 3.6
    fibs = fib(A,B)
    lenA = len(A)
    return [fibs[A[i]] % (2**B[i]) for i in range(lenA)]
