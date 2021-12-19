import heapq
from collections import defaultdict

FORWARD, BACKWARD = 0, 1

def is_visited(i):
    if i == -1:
        return False
    return True

def toggle_direction(direction):
    if direction == 0:
        return 1
    return 0

def solution(n, start, end, roads, traps):
    answer = 0
    traps = set(traps)
    # edges = [[0 for i in range(n + 1)] for i in range(n + 1)]
    edges = [[defaultdict(int) for i in range(n + 1)] for i in range(2)]
    for road in roads:
        i, j, weight = road
        if edges[FORWARD][i][j] == 0 or edges[FORWARD][i][j] > weight:
            edges[FORWARD][i][j] = weight
        if edges[BACKWARD][j][i] == 0 or edges[BACKWARD][j][i] > weight:
            edges[BACKWARD][j][i] = weight
    
    distances = [[[-1 for i in range(n + 1)] for i in range(n + 1)] for i in range(2)]
    direction = FORWARD
    q = []
    for there, weight in edges[direction][start].items():
        distances[direction][start][there] = weight
        new_direction = direction
        used_traps = set()
        if there in traps:
            new_direction = toggle_direction(new_direction)
            used_traps.add(there)
        heapq.heappush(q, (there, weight, new_direction, used_traps))
    cnt = 0
    # print(q)
    # print(edges[1][3])
    while q:
        here, distance, direction, used_traps = heapq.heappop(q)
        # print(here, distance, used_traps)
        if here == end:
            answer = distance
            break
        for there, weight in edges[FORWARD][here].items():
            if (there in used_traps) and (here not in used_traps):
                continue
            if (here in used_traps) and (there not in used_traps):
                continue
            prev_distance = distances[FORWARD][here][there]
            new_distance = distance + weight
            if is_visited(prev_distance) and prev_distance <= new_distance:
                continue
            distances[FORWARD][here][there] = new_distance
            new_direction = direction
            new_used_traps = used_traps.copy()
            if there in traps:
                if there in new_used_traps:
                    new_used_traps.remove(there)
                    new_direction = FORWARD
                else:
                    new_used_traps.add(there)
                    new_direction = BACKWARD
            # print(new_used_traps)
            heapq.heappush(q, (there, new_distance, new_direction, new_used_traps))
        for there, weight in edges[BACKWARD][here].items():
            if (there not in traps) and (here not in traps):
                continue
            if here in used_traps and there in used_traps:
                continue
            # print(4)
            prev_distance = distances[BACKWARD][here][there]
            new_distance = distance + weight
            if is_visited(prev_distance) and prev_distance <= new_distance:
                continue
            distances[BACKWARD][here][there] = new_distance
            new_direction = direction
            new_used_traps = used_traps.copy()
            if there in traps:
                if there in new_used_traps:
                    new_used_traps.remove(there)
                    new_direction = BACKWARD
                else:
                    new_used_traps.add(there)
                    new_direction = BACKWARD
            # print(new_used_traps)
            heapq.heappush(q, (there, new_distance, new_direction, new_used_traps))
    return answer