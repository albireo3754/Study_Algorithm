from itertools import combinations
import bisect

def shorten_conditions(conditions):
    result = ''
    for condition in conditions:
        if condition[0] == '-':
            result += 'a'
        else:
            result += condition[0]
    return result

def parse_info_element(_element):
    element = _element.split()
    conditions = element[:-1]
    score = element[-1]
    return conditions, int(score)

def parse_query_element(_element):
    element = _element.split(' and ')
    conditions = element[:-1]
    soul_food, score = element[-1].split()
    conditions.append(soul_food)
    return conditions, int(score)

def store(db, condition, score):
    if condition in db:
        db[condition].append(score)
    else:
        db[condition] = [score]
        
def denormalize(db):
    candidate = ['jpca', 'bfa', 'jsa', 'pca']
    for jpc in candidate[0]:
        for bf in candidate[1]:
            for js in candidate[2]:
                for pc in candidate[3]:
                    condition = jpc + bf + js + pc
                    if 'a' in condition:
                        for i in range(4):
                            if condition[i] != 'a':
                                continue
                            for j in candidate[i][:-1]:
                                n_condition = condition[:i] + j +\
                                        condition[i + 1:]
                                if condition not in db:
                                    db[condition] = db[n_condition][:]
                                else:
                                    db[condition].extend(db[n_condition[:]])
                            break
                    else:
                        if condition not in db:
                            db[condition] = []
                    db[condition].sort()
def solution(info, query):
    answer = []
    db = {}
    for info_element in info:
        conditions, score = parse_info_element(info_element)
        condition = shorten_conditions(conditions)
        # print(score)
        store(db, condition, score)
        # print(conditions, score)
        # print(shorten_conditions(conditions))
    denormalize(db)
        
    for query_element in query:
        conditions, score = parse_query_element(query_element)
        condition = shorten_conditions(conditions)
        i = bisect.bisect_left(db[condition], score)
        answer.append(len(db[condition]) - i)
        # print(db[condition])
        # print(list(db))
        # print(shorten_conditions(conditions))
    # print(db['pbsc'])
    # print(db['absa'])
    # print(db['pbsa'])
    # print(db['cbsa'])
    return answer