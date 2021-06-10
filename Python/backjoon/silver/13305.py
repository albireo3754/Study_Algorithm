import sys
input = sys.stdin.readline

N = int(input())
dist = list(map(int, input().split()))
cost = list(map(int ,input().split()))

position = 0
min_fuel = cost[0]
answer = 0
while position < N - 1:
    answer += min_fuel * dist[position]
    position += 1
    min_fuel = min(min_fuel, cost[position])
print(answer)