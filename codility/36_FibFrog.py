#58
#2 - 78 almost bfs
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
    
    # A.reverse()
    A.append(1)
    fibs = makeFibs(A)

    fibs.reverse()
    
    fibsN = len(fibs)
    # print(fibs)
    N = len(A)
    pos = [-1]
    jump = []
    cnt = 0
    curpos = -1
    back = -1
    minJump = N+1
    fibIdx = [0] * (N+1)
    fibcnt = 0
    for i in range(len(fibIdx)):
        if i in fibs:
            fibcnt += 1
        fibIdx[i] = fibsN - fibcnt
    # print(fibIdx)
    # print(fibs)
    while True:
        if back == -1:
            fibsFirst = 0
        else:
            fibsFirst = jump.pop() + 1
        back = 1
        # print(fibsFirst)
        # print(pos,jump,minJump)
        # print(N, curpos, fibsN, N-1-curpos)
        fibsFirst = max(fibsFirst, fibIdx[N-1 - curpos])
        print(fibsFirst)
        for i in range(fibsFirst,fibsN):
            
            if len(jump) >= minJump - 1:
                break       
            fib = fibs[i]
            tempos = curpos + fib 
            # print(tempos, N-1)
            if tempos == N-1:
                print(len(pos),"pos")
                if minJump > len(pos):
                    minJump = len(pos)
                    if minJump == 1 or minJump == 2:
                        return minJump
                # print(minJump)
            elif tempos < N-1:
                
                if A[tempos] == 1:

                    pos.append(tempos)
                    jump.append(i)
                    back = -1
                    break
        
        if back == 1:
            pos.pop()
            if len(pos) == 0:
                if minJump == N +1:
                    return -1
                else:
                    return minJump           
            
        curpos = pos[-1]
