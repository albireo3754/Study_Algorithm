def solution(dartResult):
    answer = 0
    before_score = 0
    power = 0
    score = 0
    for i in dartResult:
        if ord(i)>= 48 and ord(i)<=57:
            if power > 0:
                answer += before_score
                before_score = score
                score = 0
                power = 0
            if score == 1:
                score = 10
            elif score == 0:
                score = int(i)
        elif i == 'S':
            power = 1
        elif i == 'D':
            power = 2
            score = score ** 2
        elif i == 'T':
            power = 3
            score = score ** 3
        elif i == '*':
            score *= 2
            print(score)
            before_score *= 2
        elif i == '#':
            score *= -1
    print(score)
    answer += score + before_score
    return answer

#regular expression or 10 -> replace to other char
# answer를 만들때 굳이 +로 계산하지말고 list를 만들었으면 좀더 쉽게 구현했을것