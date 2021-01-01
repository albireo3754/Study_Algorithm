def solution(n, lost, reserve):
    answer = 0
    answer = n - len(lost)

    overlap=[]
    for i in lost:
        if i in reserve:
            overlap.append(i)
    for j in overlap:
        answer += 1
        reserve.remove(j)
        lost.remove(j)
    for i in lost:        
        if i - 1 in reserve:
            reserve.remove(i-1)
            answer+=1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer+=1
    return answer
    
# overlap delete
# lost = list(set(lost) - set(reserve))
# reserve = list(set(reserve) - set(lost))