from itertools import combinations

def solution(orders, course):
    answer = []
    sets = [{} for i in range(11)]
    for order in orders:
        for i in course:
            if i > len(order):
                continue
            for comb in combinations(sorted(order), i):
                set_menu = ''.join(comb)
                if set_menu in sets[i]:
                    sets[i][set_menu] += 1
                else:
                    sets[i][set_menu] = 1
    for i in course:
        max_cnt = -1
        for string, cnt in sorted(sets[i].items(), key = lambda x: -x[1]):
            print(string, cnt, i)
            if max_cnt > cnt or cnt < 2:
                break
            answer.append(string)
            max_cnt = cnt

    answer.sort()
    return answer