import re
from collections import defaultdict

def solution(user_id, banned_id):
    answer = 0
    
    counter = [set() for i in range(len(banned_id))] 
    for i, v in enumerate(banned_id):
        p = re.compile('^' + v.replace('*', '[a-z0-9]') + '$')
        for user in user_id:
            if p.match(user):
                counter[i].add(user)
    print(counter)
    answer = []
    n = len(banned_id)
    print(n)
    before = set()
    def dfs(idx):
        if idx == n:
            for i in answer:
                if before == i:
                    return
            return answer.append(before.copy())
        for j in list(counter[idx]):
            if j in before:
                continue
            before.add(j)
            dfs(idx + 1)
            before.remove(j)

    dfs(0)
    return len(answer)