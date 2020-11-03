# 1 - get 85% score => this algorithm's big O is O(N**2). I know but don't solve this problem

def solution(H):
    # write your code in Python 3.6
    
    heights = []
    wallCnt = 0
    nextHeights = []
    for wall in H:
        while wall> 0:
            for height in heights:
                if wall == 0:
                    break
                elif height> wall:
                    nextHeights.append(wall)
                    wall = 0
                    wallCnt += 1
                    break
                else:
                    wall -= height
                    nextHeights.append(height)
            if wall != 0:
                nextHeights.append(wall)
                wall = 0
                wallCnt += 1
        heights = nextHeights
        nextHeights = []
    return wallCnt


solution([8,8,5,7,9,8,7,4,8])
