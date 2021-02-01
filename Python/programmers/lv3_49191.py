from collections import defaultdict


def solution(n, results):
    edge = defaultdict(list)
    edge_reverse = defaultdict(list)

    for i in results:
        edge[i[0]].append(i[1])
        edge_reverse[i[1]].append(i[0])

    def dfs(path, edge, i):
        if i in path:
            return
        path.add(i)
        for j in edge[i]:
            dfs(path, edge, j)

    cnt = 0
    for i in range(1, n+1):
        path = set()
        path_reverse = set()
        dfs(path, edge, i)
        dfs(path_reverse, edge_reverse, i)
        if len(path) + len(path_reverse) == n + 1:
            cnt += 1
    return cnt
