def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    pre = -1
    for i in arr:
        if i != pre : 
            answer.append(i)
        pre = i 

    return answer
