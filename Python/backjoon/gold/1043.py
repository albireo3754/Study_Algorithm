import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

dont_lier = set()
for i in range(1, arr[0] + 1):
    dont_lier.add(arr[i])

party_room = []
for i in range(M):
    party_room.append(list(map(int, input().split(' ')))[1:])
visited = [1 for i in range(M)]
# print(dont_lier, party_room)
for i in range(50):
    for j in range(M):
        if visited[j] == 0:
            continue
        for people in party_room[j]:
            if people in dont_lier:
                for true_people in party_room[j]:
                    dont_lier.add(true_people)
                visited[j] = 0
                continue
# print(dont_lier, party_room)

print(sum(visited))    
