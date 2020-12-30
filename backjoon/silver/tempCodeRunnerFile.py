import queue
q = queue.Queue()

N = input()

for i in range(1, N+1):
    q.put(i)

while q.qsize() > 1:
    q.get()
    q.put(q.get())

print(q.get())