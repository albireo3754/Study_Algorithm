import sys

input = sys.stdin.readline

R, C = map(int, input().split())
rg, cg, rp, cp = map(int, input().split())
grid = [list(input().rstrip()) for i in range(R)]

# print(grid)

# def find_gp():
#     gp = {}
#     count = 0
#     for i in range(R):
#         for j in range(C):
#             if grid[i][j] == 'G' or grid[i][j] == 'P':
#                 if grid[i][j] in gp:
#                     continue
#                 count += 1
#                 gp[grid[i][j]] = (i, j)
#                 if count == 2:
#                     return gp
#     return gp

# gp = find_gp()
# # print(gp)
# rg_start, cg_start = gp['G']
# rp_start, cp_start = gp['P']

# def is_ginp(i, j):
#     if rp_start <= i < rp_start + rp and cp_start <= j < cp_start + cp:
#         return True
#     if i >= R or j >= C:
#         return True
#     return False

# def go():
#     flag = False
#     for i in range(rg):
#         for j in range(cg):
#             # print(i, j, rg_start + i , cg_start + j)
#             if grid[rg_start + i][cg_start + j] != 'G':
#                 return 0
            
#             if is_ginp(rg_start + i, cg_start + j):
#                 flag = True
#                 # print(flag)
#     if flag:
#         return 1
#     return 0
# answer = go()
# print(answer)

gp = {'G': 0, 'P': 0}

for i in range(R):
    for j in range(C):
        if grid[i][j] != '.':
            gp[grid[i][j]] += 1

if gp['G'] == rg * cg and gp['P'] != rp * cp:
    print(1)
else:
    print(0)