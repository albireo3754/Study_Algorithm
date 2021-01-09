def solution(n, s):
    if n > s:
        return [-1]
    answer = [s // n] * n
    remainder = s % n
    for i in range(1, remainder+1):
        answer[i * -1] += 1
    return answer
