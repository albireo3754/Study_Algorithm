# 100 %

def solution(A):
    discSet = []
    for idx, val in enumerate(A):
        discSet.append((idx - val , -1))
        discSet.append((idx + val, 1))
    
    discSet.sort()

    intersect = 0
    right = 1
    left = 0
    for i in discSet:
        if i[1] == 1:
            intersect += left - right 
            right += 1
        else:
            left += 1
    if intersect > 10000000:
        return -1
    return intersect

print(solution([1,5,2,1,4,0]))
