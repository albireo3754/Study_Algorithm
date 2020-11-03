#1 - 62% 



def solution(H):
    # write your code in Python 3.6
    
    heights = []
    wallCnt = 0
    for wall in H:
        while len(heights) != 0 and heights[-1] > wall:
            heights.pop()
        if len(heights) == 0 or heights[-1]<wall:
            heights.append(wall)
            wallCnt += 1
    return wallCnt

print(solution([1,2,3,2,1]))
