import sys

input = sys.stdin.readline

T = input().replace('\n', '')
P = input().replace('\n', '')

# def preprocess(text):
#     n = len(text)
#     start = 0
#     answer = [0] * (n + 1)
#     for i in range(1, n):
#         if text[i] != text[start]:
#             start = 0
#         if text[i] == text[start]:
#             start += 1
#         answer[i + 1] = start        
#     return answer

def get_pi(text):
    n = len(text)
    pi = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and text[i] != text[j]:
            j = pi[j - 1]
        if text[i] == text[j]:
            j += 1
            pi[i] = j
    return pi
p_i = 0
n = len(P)
answer = []
pi = get_pi(P)
lenT = len(T)
p_i = 0
for t_i in range(0, lenT):
    
    while p_i > 0 and P[p_i] != T[t_i]:
        p_i = pi[p_i - 1]
    if P[p_i] == T[t_i]:
        p_i += 1
        if p_i == n:
            answer.append(t_i - n + 2)
            p_i = pi[p_i - 1]

print(len(answer))
print(*answer)