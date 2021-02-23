def solution(stones, k):
    answer = 0
    left = 1
    right = 200000001
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
                if cnt == k:
                    right = mid - 1
                    break
            else:
                cnt = 0     
        else:
            answer = mid
            left = mid + 1

    return answer + 1