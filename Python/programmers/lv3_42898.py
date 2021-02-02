def solution(m, n, puddles):
    answer = 0
    routes = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for x, y in puddles:
        routes[x][y] = -1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            #puddle
            if routes[i][j] == -1:
                continue
            #init
            if i == 1 and j == 1:
                routes[i][j] = 1
                continue

            #max 0 => delete puddle
            routes[i][j] = (max(routes[i - 1][j], 0) + max(routes[i][j - 1], 0)) 
    return routes[m][n] % 1000000007