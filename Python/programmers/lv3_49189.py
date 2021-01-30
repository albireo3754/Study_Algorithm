from collections import defaultdict, deque
def solution(n, edge):
    vertex = defaultdict(list)
    cnt_dict = defaultdict(int)
    for i in edge:
        vertex[i[0]].append(i[1])
        vertex[i[1]].append(i[0])

    q = deque([(1, 0)])
    visited = set()
    answer = 0
    while q:
        node, cnt = q.popleft()
        if node in visited:
            continue
        visited.add(node)
        cnt_dict[cnt] += 1
        for i in vertex[node]:
            if i in visited:
                continue
            flag = 1
            q.append((i, cnt + 1))

    print(*cnt_dict)
    return cnt_dict[[*cnt_dict][-1]]
