import collections

def solution(skill, skill_trees):
    answer = len(skill_trees)
    for skill_tree in skill_trees:
        skill_q = collections.deque(skill)
        for pre_skill in skill_tree:
            if len(skill_q) == 0:
                break
            if pre_skill in skill_q and pre_skill != skill_q.popleft():
                answer -= 1
                break

    return answer

