def solution(N, number):
    memo = [set([]) for _ in range(9)]
    for i in range(1, 9):
        cnt = i - 1
        num = 0
        while cnt >= 0:
            num += (10 ** cnt) * N
            cnt -= 1
        memo[i].add(num)

    if N == number:
        return 1
    for now_idx in range(2, 9):
        left = 1
        right = now_idx - left
        while left <= right:
            for i in memo[left]:
                for j in memo[right]:
                    if i < j:
                        a, b = j, i
                    else:
                        a, b = i, j
                    memo[now_idx].add(a + b)
                    memo[now_idx].add(a - b) if a - b > 0 else 0
                    memo[now_idx].add(a * b)
                    memo[now_idx].add(a // b) if a // b > 0 else 0
            if number in memo[now_idx]:
                return now_idx
            left += 1
            right -= 1
    return -1

2021 프로그래머스
