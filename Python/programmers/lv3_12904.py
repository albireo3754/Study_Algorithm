def solution(s):
    answer = 0
    sub_length = len(s)
    left = 0
    right = sub_length
    while sub_length > 0:
        left = 0
        right = sub_length
        mid = (left + right) // 2 

        while right <= len(s):
            for i in range(0, mid):
                if s[left + i] != s[right - 1 - i]:
                    break
                if s[left + i] == s[right - 1 - i] and i == mid - 1:
                    return sub_length
            left += 1
            right += 1
        sub_length -= 1

    return 1