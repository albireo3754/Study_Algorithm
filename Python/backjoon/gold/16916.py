import sys

input = sys.stdin.readline

pi = []

str1 = input().rstrip()
str2 = input().rstrip()

def get_pi(M):
    m = len(M)
    pi = [0 for i in range(m)]
    idx = 0
    for i in range(1, m):
        while idx > 0 and M[i] != M[idx]:
            idx = pi[idx - 1]
        if M[i] == M[idx]:
            idx += 1
            pi[i] = idx
    return pi

def kmp(N, M):
    n = len(N)
    m = len(M)

    pi = get_pi(M)

    idx = 0
    for i in range(0, n):
        while idx > 0 and N[i] != M[idx]:
            idx = pi[idx - 1]
        if N[i] == M[idx]:
            if idx == m - 1:
                return 1
            else:
                idx += 1
    # while start + idx < n:
    #     if idx < m and N[start + idx] == M[idx]:
    #         idx += 1
    #         if idx == m:
    #             return 1
    #     else:
    #         if idx == 0:
    #             start += 1
    #         else:
    #             start += idx - pi[idx - 1]
    #             idx = pi[idx - 1]
    return 0
# if str1 == str2:
#     print(1)
# else:
print(kmp(str1, str2))