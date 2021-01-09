#42576

def solution(participant, completion):
    hashtable = {}
    for i in participant:
        if hashtable.get(i):
            hashtable[i] += 1
        else:
            hashtable[i] = 1
    for i in completion:
        hashtable[i] -= 1
        if hashtable[i] == 0:
            del hashtable[i]
    return list(hashtable)[0]


# anoter solution
# import collections

# def solution(participant, completion):
#     answer = collections.Counter(participant) -
#             collections.Counter(completion)
#     return list(answer)[0]
