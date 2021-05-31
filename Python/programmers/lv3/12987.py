import heapq
def solution(A, B):
    pq = []
    teamA = 0
    teamB = 1
    A = sorted(A)
    for i in A:
        heapq.heappush(pq, (i, teamA))
    for i in B:
        heapq.heappush(pq, (i, teamB))

    answer = 0
    temp = 0

    AB = [0, 0]
    N = len(A)
    mina = 0
    while pq:
        num, team = heapq.heappop(pq)
        AB[team] += 1
        # print(num, team)
        if team == teamA:
            temp += 1
        else:
            if temp == 0:
                continue
            if A[mina] >= num:
                continue
            mina += 1
            temp -= 1
            answer += 1

    return answer