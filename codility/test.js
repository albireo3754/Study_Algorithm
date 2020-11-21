def solution(A):
    discSet = sorted([(idx - var, idx + var) for idx, var in enumerate(A)])
    print(discSet)
    
console.log(solution([0, 1, 0, 1, 1]));
