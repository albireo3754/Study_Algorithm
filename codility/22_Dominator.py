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
    
    if len(domiCandis) == 0:
        return -1
        
    domiCandi = domiCandis[0]
    
    for i, v in enumerate(A):
        if domiCandis[0] == v:
            domiIdx.append(i)
    
    if len(domiIdx) > len(A)//2:
        return domiIdx[0]
    else:
        return -1
