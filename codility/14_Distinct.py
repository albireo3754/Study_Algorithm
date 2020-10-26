# 91%
# extreme extreme_empty problem: there is no none array Array condition
# so correct lenA if lenA == 0
# 100%

def solution(A):
    A.sort()
    resert = 1
    lenA = len(A)
    if lenA <= 1:
        return lenA

    for idx in range(1,lenA):
        if A[idx-1] != A[idx]:
            resert += 1
    return resert

print(solution([2,1,1,2,3,1]))