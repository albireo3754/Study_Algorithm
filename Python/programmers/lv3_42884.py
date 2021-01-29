def solution(routes):
    answer = 1
    routes.sort(key = lambda x: x[0])
    print(routes)
    temp_end = routes[0][1]
    for i in routes:
        if temp_end < i[0]:
            temp_end = i[1]
            answer += 1
            continue
        temp_end = min(temp_end, i[1])
    return answer
