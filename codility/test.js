def solution(A):
    discSet = sorted([(idx - var, idx + var) for idx, var in enumerate(A)])
    print(discSet)
    