import math
def solution(progresses, speeds):
    answer = []
    can_deploy = 0
    day_left = 0
    for i, v in enumerate(progresses):
        if day_left == 0:
            day_left = math.ceil((100 - v)/speeds[i])
            can_deploy += 1
            continue
        if day_left >= math.ceil((100 - v)/speeds[i]):
            can_deploy += 1
        else:
            answer.append(can_deploy)
            day_left = math.ceil((100 - v)/speeds[i])
            can_deploy = 1
    answer.append(can_deploy)
    return answer