def solution(n, times):
    times.sort()
    left = 1
    right = times[-1] * n
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for time in times:
            cnt += mid // time
            if cnt >= n:
                break
        if cnt >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer
