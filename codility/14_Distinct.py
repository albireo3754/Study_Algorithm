# 91%

def solution(A):
    A.sort()
    resert = 1
    if len(A) == 1:
        return 1

    for idx in range(1,len(A)):
        if A[idx-1] != A[idx]:
            resert += 1
    return resert

print(solution([2,1,1,2,3,1]))