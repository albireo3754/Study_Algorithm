import math

def solution(N):
    # write your code in Python 3.6
    count = 0
    i = 1
    
    while i < math.sqrt(N):
        if N % i == 0:
            count += 1
        i += 1
    count *= 2
    
    if i == math.sqrt(N):
        count += 1
        
    return count
    
