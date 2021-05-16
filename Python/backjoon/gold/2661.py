# N = int(input())

# answer = ''
# for i in range(N):
#     if i & 1:
#         if i % 4 == 1:
#             answer += '2'
#         elif i % 4 == 3:
#             answer += '3'
#     else:
#         answer += '1'

# print(int(answer), end='')

N = int(input())

answer = [1 for i in range(N)]

def terinary_sum_1(arr):
    carry = 1
    n = 1
    result = [*arr]
    for i in range(len(arr) - 1, -1, -1):
        if carry == 0:
            break
        if result[i] + n > 3:
            carry = 1
            result[i] = 1
        else:
            carry = 0
            result[i] += n
    return result

#test terinary_sum
# print(terinary_sum_1([1,3,3]))

for i in range(1, len(answer) + 1):
    for j in range(0, i):
        test = answer[0:i - j]
        # print(test, j, i)
        while True:
            m = len(test) // 2
            for k in range(1, m + 1):
                # print('tst',test[-1: -1 - k : -1])
                if test[-1: -1 - k : -1] == test[-1 - k : -1 - 2 * k : -1]:
                    flag = False
                    break
                else:
                    flag = True
            else:
                break
            test = terinary_sum_1(test)
        answer[0: i - j] = test

str_answer = ''
for i in answer:
    str_answer += str(i)
print(str_answer)
        
