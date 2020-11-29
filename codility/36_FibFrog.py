# 58

def makeFibs(A):
    fibs = []
    fibs.append(1)
    fibs.append(2)
    fib = 1
    N = len(A) + 1

    for i in range(2,N):
        fib = fibs[i-1] + fibs[i-2]
        if fib > N :
            break
        fibs.append(fib)

    return fibs    

def solution(A):
    # write your code in Python 3.6
    
    A.append(1)
    fibs = makeFibs(A)
    fibs.reverse()
    fibsN = len(fibs)
    N = len(A)
    pos = [-1]
    jump = []
    cnt = 0
    curpos = -1
    back = -1

    while True:
        if back == -1:
            fibsFirst = 0
        else:
            fibsFirst = jump.pop() + 1
        back = 1
        # print(fibsFirst)
        # print(pos,jump)
        for i in range(fibsFirst,fibsN):
            fib = fibs[i]
            
            tempos = curpos + fib 
            # print(tempos,"tem")
            if tempos == N - 1:
                return len(pos)
            elif tempos < N - 1:
                if A[tempos] == 1:
                    pos.append(tempos)
                    jump.append(i)
                    back = -1
                    break
        
        if back == 1:
            pos.pop()

        if len(pos) == 0:
            return -1           
            
        curpos = pos[-1]
