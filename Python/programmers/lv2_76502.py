from collections import deque

def solution(s):
    answer = 0
    stack = []
    brackets = {'(' : ')', '{' : '}', '[' : ']'}
    q = deque(s)
    # print(q)
    for _ in range(len(q)):
        flag = False
        for i in q:
            # print(i)
            if i in '[({':
                stack.append(i)
            else:
                if stack:
                    if brackets[stack[-1]] == i:
                        stack.pop()
                    else:
                        flag = True
                        break
                else:
                    flag = True
                    break
        q.append(q.popleft())        
        if flag or stack:
            continue
        answer += 1
        
    return answer