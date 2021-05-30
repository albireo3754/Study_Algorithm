import sys

input = sys.stdin.readline

N, T = map(int, input().split())

#1~T
turns = list(map(int, input().split()))

friends_acquire_card = {}
friends_number_card = {}
private = set()

for i in range(1, N + 1):
    friends_acquire_card[i] = set()
    friends_number_card[i] = set()

for i in range(T):
    _input = input().split()
    dummy_id, cmd, cmd_id = [0, '', -1]
    if len(_input) == 2:
        dummy_id, cmd = _input
        print(dummy_id)
        continue
    dummy_id, cmd, cmd_id = _input
    if cmd == 'acquire':
        if cmd_id not in private:
            friends_number_card[turns[i]].add(cmd_id)
            private.add(cmd_id)
        else:
            friends_acquire_card[turns[i]].add(cmd_id)
        print(dummy_id)
        continue
    
    if cmd == 'release':
        friends_number_card[turns[i]].remove(cmd_id)
        private.remove(cmd_id)
        print(dummy_id)
        continue
    # print(dummy_id, cmd, cmd_id)
