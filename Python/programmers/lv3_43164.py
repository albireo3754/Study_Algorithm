# from collections import defaultdict
# def solution(tickets):
#     tickets.sort(key = lambda x: x[1])
#     q = defaultdict(list)
    
#     for i, v in enumerate(tickets):
#         q[v[0]].append([i, v])
    
#     print(q)
#     answer = []
#     path = [0 for _ in range(len(tickets))]
#     def dfs(path, visited, depart):
#         # print(path, visited, depart)
#         if sum(path) == len(tickets):
#             answer.extend(visited)
#             # print(visited)
#             return 1
#         for i, v in q[depart]:
#             if path[i]:
#                 continue
#             path[i] = 1
#             if dfs(path[:], visited[:] + [v[1]], v[1]):
#                 return 1
#             dfs(path[:], visited[:] + [v[1]], v[1])
#             path[i] = 0
#         return 0
#     dfs(path[:], ["ICN"], "ICN")
#     return answer
from collections import deque
def solution(tickets):
    answer = []
    edge = {}
    tickets.sort(reverse = True)
    for departure, destination in tickets:
        if departure in edge:
            edge[departure].append(destination)
        else:
            edge[departure] = deque([destination])

    TICKETS_NUM = len(tickets)

    answer = []
    answer.append("ICN")

    def dfs(departure):
        if len(answer) == TICKETS_NUM + 1:
            return True
        if departure not in edge:
            return False

        for _ in range(len(edge[departure])):
            destination = edge[departure].pop()
            answer.append(destination)
            flag = dfs(destination)
            if flag:
                return True
            answer.pop()
            edge[departure].appendleft(destination)
        return False
    dfs("ICN")

    return list(answer)

print(solution([["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]))
# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))