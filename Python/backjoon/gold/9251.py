import sys

input = sys.stdin.readline
A = ['']
A.extend(list(input().rstrip()))
B = ['']
B.extend(list(input().rstrip()))
lcs = [[0 for i in range(len(A))] for i in range(len(B))]

for i in range(1, len(lcs)):
    for j in range(1, len(lcs[0])):
        if A[j] == B[i]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])

print(lcs[-1][-1])