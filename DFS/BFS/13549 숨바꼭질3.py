from collections import deque
import sys

n, k = map(int, input().split())
visited = [0 for _ in range(100001)] 
min_time = sys.maxsize

queue = deque()
queue.append((n, 0))
visited[n] = 1

while queue:
    x, time = queue.popleft()
    visited[x] = 1

    if x == k:
        min_time = min(min_time, time)

    if 0 <= x-1 < 100001 and visited[x-1] == 0:
        queue.append((x-1, time+1))
        
    if 0 <= x+1 < 100001 and visited[x+1] == 0:
        queue.append((x+1, time+1))
        
    if 0 <= 2*x < 100001 and visited[2*x] == 0:
        queue.append((2*x, time))

print(min_time)