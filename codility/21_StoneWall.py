# 1 - get 85% score => this algorithm's big O is O(N**2). I know but don't solve this problem
# 2 - get 100% score => i think this problem like picture of problem. verticular box pile up. because of this approch, i got n**2

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

solution([8,8,5,7,9,8,7,4,8])
