def solution(n):
    answer = 0
    tri = ''
    while n > 0:
        tri = str(n % 3) + tri 
        n = n // 3 


    for i, v in enumerate(map(int, tri)):
        answer += v * (3 ** i)
    return answer
