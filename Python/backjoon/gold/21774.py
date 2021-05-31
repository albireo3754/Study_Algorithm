import sys
import bisect

input = sys.stdin.readline

N, Q = map(int, input().split())

# 1 , 2, 3, 4, 5, 6, 7,
Months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def d_to_s(D):
    y, m, d = map(int, D.split('-'))
    # leap = 1
    # if y > 2000:
    #     y = (y - 1 - 2000) * 365 + ((y - 1 - 2000) // 4 + leap) * 366
        
    # else:
    #     y = 0
    # if m > 2 and (y - 2000) % 4 == 0:
    #     m = sum(Months[0:m]) + 1
    # else:
    #     m = sum(Months[0:m])
    # return (y + m + d) * 3600 * 24
    y -= 1999
    return y * 1e10 + m * 1e8 + d * 1e6
def h_to_s(H):
    h, m, s = map(int, H.split(':'))
    return h * 1e4 + m * 1e2 + s
    # return h * 3600 + m * 60 + s

lv = [[] for i in range(7)]
def time_to_s(t):
    # print(t)
    timearr = t.split()
    return d_to_s(timearr[0]) + h_to_s(timearr[1])
for i in range(N):
    time, level = input().split('#')
    level = int(level)
    # time = time_to_s(time)
    # print(time, level)
    lv[level].append(time)
for i in lv:
    i.sort()


for j in range(Q):
    time1, time2, level = input().split('#')
    # print(time1, 'time1',time2)
    # time1 = time_to_s(time1)
    # time2 = time_to_s(time2)
    level = int(level)
    res = 0
    for i in range(level, 7):
        lower_bound = bisect.bisect_left(lv[i], time1)
<<<<<<< HEAD
        upper_bound = bisect.bisect_left(lv[i], time2)
=======
        upper_bound = bisect.bisect_right(lv[i], time2)
>>>>>>> Simulation
        res += upper_bound - lower_bound
    print(res)

# print(d_to_s('2000-1-1'))
# print(h_to_s('23:59:59'))