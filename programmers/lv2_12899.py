def solution(n):
    answer = ''
    while n > 0:
        changed, n = (n % 3, n // 3) if n % 3 != 0 else (4, n // 3 - 1)
        answer = str(changed) + answer
    return answer