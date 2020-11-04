# 50% -> odd number returns -1

def solution(A):
    # write your code in Python 3.6
    
    domiIdx = []
    domiCandis = []
    
    for v in A:
        if len(domiCandis) == 0:
            domiCandis.append(v)
        else:
            if domiCandis[-1] == v:
                domiCandis.append(v)
            else:
                domiCandis.pop()
    
    if len(domiCandis) < 2: 
        return -1
    
    for i, v in enumerate(A):
        if domiCandis[0] == v:
            domiIdx.append(i)
    return domiIdx[0]
    
