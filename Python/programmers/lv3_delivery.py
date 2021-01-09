import heapq

def make_edges(road):
    edges = {}
    for (a,b,w) in road:
        edges[a] = edges.get(a, []) + [(b, w)]
        edges[b] = edges.get(b, []) + [(a, w)]
    return edges

def solution(N, road, K):
    answer = 0
    INF = float("inf")
    distance = [INF] * (N + 1)
    distance[1] = 0
    queue = []
    edges = make_edges(road)
    heapq.heappush(queue,[0,1])
    processed = [0] * (N + 1)
    while queue:
        node = heapq.heappop(queue)[1]
        if processed[node]:
            continue
        processed[node] = 1
        for arrive, weight in edges[node]:
            if distance[arrive] > weight + distance[node]:
                distance[arrive] = weight + distance[node]
                heapq.heappush(queue,[distance[arrive],arrive])
    for i in distance:
        if i <= K:
            answer += 1
    return answer