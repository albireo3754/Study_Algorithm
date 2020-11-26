# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, M):
    # write your code in Python 3.6
    X = 0
    wrapper = []
    cnt = 0
    while not(X in wrapper):
        wrapper.append(X)
        X = (X+M)%N
        cnt += 1

    return cnt
