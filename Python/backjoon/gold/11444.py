a = 0
b = 1
c = 1

n = int(input())

def matrix_mul(a, b):
    k = [[0, 0], [0, 0]]
    for i in range(len(k)):
        for j in range(len(k[0])):
            temp = 0
            for t in range(2):
                temp += a[i][t] * b[t][j] 
            k[i][j] = temp % 1000000007
    return k

# print(matrix_mul([[1,2], [3,4]], [[2, -4], [1, 3]]))
def matrix_pow(matrix, n):
    I = [[1, 0], [0, 1]]
    while n > 0:
        # 홀수체크
        if n & 1:
            # print(n, I, matrix)
            I = matrix_mul(I, matrix)
        matrix = matrix_mul(matrix, matrix)
        n = n // 2
    return I

print(matrix_pow([[1, 1], [1, 0]], n)[0][1])