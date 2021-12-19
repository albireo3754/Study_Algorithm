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
        if here == end:
            answer = distance
            break
        for there, weight in edges[direction][here].items():
            # print(here, there, weight)
            prev_distance = distances[direction][here][there]
            new_distance = distance + weight
            # print(here, there, direction, prev_distance, new_distance, used_traps)
            if is_visited(prev_distance) and prev_distance <= new_distance:
                continue
            distances[direction][here][there] = new_distance
            new_direction = direction
            new_used_traps = used_traps.copy()
            if there in traps:
                if there in new_used_traps:
                    new_used_traps.remove(there)
                else:
                    new_used_traps.add(there)
                    new_direction = toggle_direction(direction)
            else:
                new_direction = FORWARD
            heapq.heappush(q, (there, new_distance, new_direction, new_used_traps))
        direction = toggle_direction(direction)
        for there, weight in edges[direction][here].items():
            # print(here, there, weight)
            if there not in new_used_traps:
                continue
            prev_distance = distances[direction][here][there]
            new_distance = distance + weight
            # print(here, there, direction, prev_distance, new_distance, used_traps)
            if is_visited(prev_distance) and prev_distance <= new_distance:
                continue
            distances[direction][here][there] = new_distance
            new_direction = direction
            new_used_traps = used_traps.copy()
            if there in traps:
                if there in new_used_traps:
                    new_used_traps.remove(there)
                else:
                    new_used_traps.add(there)
                    new_direction = toggle_direction(direction)
            else:
                new_direction = FORWARD
            heapq.heappush(q, (there, new_distance, new_direction, new_used_traps))
    return answer