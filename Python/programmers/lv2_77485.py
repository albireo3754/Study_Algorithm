def swap(a, b):
    a, b = b, a
    return a, b

def rotate(grid, x1, y1, x2, y2):
    x1 -= 1
    y1 -= 1
    temp = grid[x1][y1]
    result = temp
    for j in range(y1 + 1, y2):
        temp, grid[x1][j] = swap(temp, grid[x1][j])
        result = min(result, temp)

    for i in range(x1 + 1, x2):
        temp, grid[i][y2 - 1] = swap(temp, grid[i][y2 - 1])
        result = min(result, temp)

    for j in range(y2 - 2, y1 - 1, -1):
        temp, grid[x2 - 1][j] = swap(temp, grid[x2 - 1][j])
        result = min(result, temp)

    for i in range(x2 - 2, x1, -1):
        temp, grid[i][y1] = swap(temp, grid[i][y1])
        result = min(result, temp)

    grid[x1][y1] = temp
    return result

def solution(rows, columns, queries):
    answer = []
    grid = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    # print(grid)
    # for i in range(rows):
    #     for j in range(columns):
    #         pass
    # rotate(grid, 1, 1, 2, 2)
    # for i in grid:
        # print(i)
    for query in queries:
        temp = 0
        x1, y1, x2, y2 = query
        temp = rotate(grid, x1, y1, x2, y2)
        answer.append(temp)

    return answer