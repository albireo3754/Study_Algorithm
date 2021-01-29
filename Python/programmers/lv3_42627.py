import heapq
from collections import deque

def solution(jobs):
    N = len(jobs)
    jobs.sort(key = lambda x: (x[0], x[1]))
    jobs = deque(jobs)
    jobs_done, done_time, waits, q = 0, 0, 0, []
    
    while jobs_done < N:
        if not q:
            request, time = jobs.popleft()
            done_time = request + time
            waits += time
        else:
            time, request = heapq.heappop(q)
            done_time += time
            waits += done_time - request
        
        jobs_done += 1
        
        while jobs and jobs[0][0] < done_time:
            heapq.heappush(q, jobs.popleft()[::-1])
            
    return waits // N
