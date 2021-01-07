import collections

def solution(bridge_length, weight, truck_weights):

    truck_crossing = collections.deque()
    len_truck = len(truck_weights)
    truck_wating = collections.deque(truck_weights)
    answer_time = 1
    truck_crossed = []
    weight_crossing = 0
    while True:
        if len(truck_crossing) == 0 or (len(truck_wating) != 0 and weight_crossing + truck_wating[0] <= weight):
            weight_crossing += truck_wating[0]
            truck_crossing.append((truck_wating.popleft(),answer_time))

        answer_time += 1
        if len(truck_crossing) > 0 and answer_time - truck_crossing[0][1] == bridge_length: 
            truck_crossed.append(truck_crossing.popleft())
            weight_crossing -= truck_crossed[-1][0]
            if len(truck_crossed) == len_truck:
                break


    return answer_time
