from collections import deque
def solution(priorities, location):
    answer = 0

    prioriti = []
    for i in sorted(priorities):
        prioriti.append(i)
    max_prioriti = prioriti.pop()
    q = deque()
    print(prioriti)
    for i, v in enumerate(priorities):
        q.append([i, v])
    request = location
    document = -1
    while request != document:
        print_ = q.popleft()
        if print_[1] == max_prioriti:
            answer += 1
            document = print_[0]
            if len(prioriti) == 0:
                return answer
            max_prioriti = prioriti.pop()
        elif print_[1] != max_prioriti:
            q.append(print_)

    return answer