for j in range(1, M + 1):
#     for i in range(N, 0, -1):
#         if grid[i][j] < grid[i + 1][j]:
#             answer[i][j] += answer[i + 1][j]
#     for i in range(1, N + 1):
#         if grid[i][j] < grid[i][j - 1]:
#             answer[i][j] += answer[i][j - 1]
#         if grid[i][j] < grid[i - 1][j]:
#             answer[i][j] += answer[i - 1][j]