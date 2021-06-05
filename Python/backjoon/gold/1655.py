import sys
import heapq
input = sys.stdin.readline

N = int(input())

low = []
high = []
for i in range(N):
    subin = int(input())
    # heapq.heappush(low, -subin)
    # if len(low) > len(high) + 1:
    #     top = -heapq.heappop(low)
    #     heapq.heappush(high, low)
    if i == 0:
        low.append(-subin)
    else:
        if len(low) == len(high):
            if subin > high[0]:
                heapq.heappush(high, subin)
                top = heapq.heappop(high)
                heapq.heappush(low, -top)
            else:
                heapq.heappush(low, -subin)
        elif len(low) == len(high) + 1:
            if subin >= -low[0]:
                heapq.heappush(high, subin)
            else:
                heapq.heappush(low, -subin)
                top = -heapq.heappop(low)
                heapq.heappush(high, top)
    print(-low[0])