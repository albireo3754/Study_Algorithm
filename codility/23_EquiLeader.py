# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    leader = 0
    leaderCandis = []
    
    lengthLeader = 0
    frontLeader = 0
    lengthA = len(A)
    
    equiCnt = 0

    for i in A:
        if len(leaderCandis) == 0 or leaderCandis[-1] == i:
            leaderCandis.append(i)
        else:
            leaderCandis.pop()
            
    if len(leaderCandis) != 0:
        leader = leaderCandis[0]
    else:#no leader?
        return 0
        
    for v in A:
        if v == leader:
            lengthLeader += 1
    
    for i, v in enumerate(A):
        #i is number leader
        #v is total number
        if v == leader:
            frontLeader += 1
        
        if frontLeader>(i+1)//2 and lengthLeader - frontLeader > (lengthA - i - 1)// 2:
            equiCnt += 1
            
    return equiCnt
