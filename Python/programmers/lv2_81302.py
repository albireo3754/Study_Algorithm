DIRECTION = ((1, 0), (0, 1), (-1, 0), (0, -1))
PARTICIPANT = "P"
TABLE = "O"
PARTITION = "X"

def solution(places):
    answer = []
    for place in places:
        grid = list(map(lambda x: list(x), place))
        N = len(grid)
        M = len(grid[0])
        
        def follow(T):
            i, j = T
            tables = []
            for di, dj in DIRECTION:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    if grid[ni][nj] == TABLE:
                        tables.append((ni, nj, di, dj))
                    if grid[ni][nj] == PARTICIPANT:
                        return False
            for i, j, bi, bj in tables:
                for di, dj in DIRECTION:
                    ni, nj = i + di, j + dj
                    if bi * -1 == di and bj * -1 == dj:
                        continue
                    if 0 <= ni < N and 0 <= nj < M:
                        if grid[ni][nj] == PARTICIPANT:
                            print(ni, nj, "n")
                            return False
            return True
        
        flag = False
        for i in range(N):
            for j in range(M):
            	if grid[i][j] == PARTICIPANT:
                    if not follow((i, j)):
                        flag = True
                        print(i,j)
                        break
            if flag == True:
                break
        if flag:
            answer.append(0)
        else:
            answer.append(1)
    return answer