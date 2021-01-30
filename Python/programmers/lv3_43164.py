from collections import defaultdict
def solution(tickets):
    tickets.sort(key = lambda x: x[1])
    q = defaultdict(list)
    
    for i, v in enumerate(tickets):
        q[v[0]].append([i, v])
    
    print(q)
    answer = []
    path = [0 for _ in range(len(tickets))]
    def dfs(path, visited, depart):
        # print(path, visited, depart)
        if sum(path) == len(tickets):
            answer.extend(visited)
            # print(visited)
            return 1
        for i, v in q[depart]:
            if path[i]:
                continue
            path[i] = 1
            if dfs(path[:], visited[:] + [v[1]], v[1]):
                return 1
            dfs(path[:], visited[:] + [v[1]], v[1])
            path[i] = 0
        return 0
    dfs(path[:], ["ICN"], "ICN")
    return answer
